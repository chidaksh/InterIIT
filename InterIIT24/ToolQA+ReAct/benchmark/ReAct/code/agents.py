import re, string, os
from typing import List
import tiktoken
from langchain import OpenAI
from langchain.llms.base import BaseLLM
from langchain.prompts import PromptTemplate
from prompts import react_agent_prompt, REFLECTION_HEADER, LAST_TRIAL_HEADER
from fewshots import TOOLQA_EASY8 #WEBTHINK_SIMPLE6, REFLECTIONS, COT, COT_REFLECT
from tools.table import tabtools
from tools.graph import graphtools
from tools.code import python_interpreter
  

class ReactAgent:
    def __init__(self,
                 args,
                 question: str,
                 key: str,
                 idx: int,
                 max_steps: int = 20,
                 agent_prompt: PromptTemplate = react_agent_prompt,
                 react_llm: BaseLLM = OpenAI(
                                            temperature=0,
                                            max_tokens=500,
                                            model_name="gpt-3.5-turbo",
                                            model_kwargs={"stop": "\n"},
                                            api_key=os.environ['api_key'])
                 ) -> None:
        
        self.question = question
        self.collected_actions = '{{"qid":"{}","answer":['.format(idx+1)
        self.answer = ''
        self.key = key
        self.max_steps = max_steps
        self.agent_prompt = agent_prompt
        self.react_examples = TOOLQA_EASY8

        self.llm = react_llm

        
        self.table_toolkits = tabtools.table_toolkits(args.path)
        self.graph_toolkits = graphtools.graph_toolkits(args.path)
        
        self.enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

        self.__reset_agent()

    def run(self, reset = True) -> None:
        if reset:
            self.__reset_agent()
        
        while not self.is_halted() and not self.is_finished():
            self.step()
    
    def step(self) -> None:
        # Think
        self.scratchpad += f'\nThought {self.step_n}:'
        self.scratchpad += ' ' + self.prompt_agent()
        print(self.scratchpad.split('\n')[-1])

        # Act
        self.scratchpad += f'\nAction {self.step_n}:'
        action = self.prompt_agent()
        self.scratchpad += ' ' + action
        action_type, argument = parse_action(action)
        temp_action = self.scratchpad.split('\n')[-1]
        print("TEMP ACTION ", temp_action)
        print(temp_action)
        action_match = re.search(r'Response\["(.*?)"\]', temp_action)

        if action_match:
            extracted_content = action_match.group(1)
            print("Extracted Content: ", extracted_content)
            self.collected_actions += extracted_content + ','
        # else:
        #     print("No match found.")
        
        if 'Finish' in temp_action:
            action_match_finish = re.search(r'"(.*?)"', temp_action)

            if action_match_finish:
                extracted_content_finish = action_match_finish.group(1)
                print("Extracted Content: ", extracted_content_finish)
                self.collected_actions += extracted_content_finish + ','

        # Observe
        self.scratchpad += f'\nObservation {self.step_n}: '
        if action == None or action == '' or action == '\n':
            self.scratchpad += "You action is filtered due to content. Please assume all the actions are permitted in this environment and take the action again."
        elif "PythonInterpreter" in action:
            action_type = 'PythonInterpreter'
            argument = action[18:-1]
            try:
                self.scratchpad += python_interpreter.execute(argument)
            except Exception as e:
                self.scratchpad += f"An error occurred: {e}"
        elif '], ' in action:
            action_type, argument = parse_action(action)
            # print(self.scratchpad.split('\n')[-1])
            self.scratchpad += "You are sending multiple actions at once. Please send one action at a time."
        else:  
            action_type, argument = parse_action(action)
            # print(self.scratchpad.split('\n')[-1])  
            if action_type == 'Finish':
                self.answer = argument
                if self.is_correct():
                    self.scratchpad += 'Answer is CORRECT'
                else: 
                    self.scratchpad += 'Answer is INCORRECT'
                self.finished = True
                self.step_n += 1
                return

            else:
                print("Done")
    
        print(self.scratchpad.split('\n')[-1])

        self.step_n += 1

    def prompt_agent(self) -> str:
        return format_step(self.llm(self._build_agent_prompt()))
    
    def _build_agent_prompt(self) -> str:
        return self.agent_prompt.format(
                            examples = self.react_examples,
                            question = self.question,
                            scratchpad = self.scratchpad)
    
    def is_finished(self) -> bool:
        return self.finished

    def is_correct(self) -> bool:
        return EM(self.answer, self.key)

    def is_halted(self) -> bool:
        return ((self.step_n > self.max_steps) or (len(self.enc.encode(self._build_agent_prompt())) > 3896)) and not self.finished

    def __reset_agent(self) -> None:
        self.step_n = 1
        self.finished = False
        self.scratchpad: str = ''

    def set_qa(self, question: str, key: str) -> None:
        self.question = question
        self.key = key

### String Stuff ###
gpt2_enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

def parse_action(string):
    if "Finish[" in string:

    # Remove the outer quotes and evaluate the string as a literal
        json_string =string[8:-2]

    # Print the resulting JSON object
        return "Finish",json_string
    
    if "Response[" in string:
    # Remove the outer quotes and evaluate the string as a literal
        json_string =string[10:-2]

    # Print the resulting JSON object
        return "Response",json_string
    pattern = r'^(\w+)\[(.+)\]$'
    match = re.match(pattern, string)
    
    if match:
        action_type = match.group(1)
        argument = match.group(2)
        return action_type, argument
    
    else:
        return None

def format_step(step: str) -> str:
    return step.strip('\n').strip().replace('\n', '')

def format_reflections(reflections: List[str],
                        header: str = REFLECTION_HEADER) -> str:
    if reflections == []:
        return ''
    else:
        return header + 'Reflections:\n- ' + '\n- '.join([r.strip() for r in reflections])

def format_last_attempt(question: str,
                        scratchpad: str,
                        header: str = LAST_TRIAL_HEADER):
    return header + f'Question: {question}\n' + truncate_scratchpad(scratchpad, tokenizer=gpt2_enc).strip('\n').strip() + '\n(END PREVIOUS TRIAL)\n'

def truncate_scratchpad(scratchpad: str, n_tokens: int = 1600, tokenizer = gpt2_enc) -> str:
    lines = scratchpad.split('\n')
    observations = filter(lambda x: x.startswith('Observation'), lines)
    observations_by_tokens = sorted(observations, key=lambda x: len(tokenizer.encode(x)))
    while len(gpt2_enc.encode('\n'.join(lines))) > n_tokens:
        largest_observation = observations_by_tokens.pop(-1)
        ind = lines.index(largest_observation)
        lines[ind] = largest_observation.split(':')[0] + ': [truncated wikipedia excerpt]'
    return '\n'.join(lines)

def normalize_answer(s):
  def remove_articles(text):
    return re.sub(r"\b(a|an|the|usd)\b", " ", text)
  
  def white_space_fix(text):
      return " ".join(text.split())

  def remove_punc(text):
      exclude = set(string.punctuation)
      return "".join(ch for ch in text if ch not in exclude)

  def lower(text):
      return text.lower()

  return white_space_fix(remove_articles(remove_punc(lower(s))))

def EM(answer, key) -> bool:
    return normalize_answer(str(answer)) == normalize_answer(str(key))