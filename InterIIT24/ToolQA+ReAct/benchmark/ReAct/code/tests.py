import os, json
import argparse
import jsonlines
from util import summarize_react_trial, log_react_trial, remove_fewshot
import datetime
import random
current_datetime = datetime.datetime.now()
datetime_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# root = '{}/benchmark/ReAct/root'
parser = argparse.ArgumentParser("")
parser.add_argument("--dataset", type=str, default="flight")
parser.add_argument("--hardness", type=str, default="easy")


parser.add_argument("--api_key", type=str, default="")

parser.add_argument("--path", type=str, default="./../../..")

parser.add_argument("--wolframalpha_api_key", type=str, default="<WOLFALPHA_API_KEY>")
parser.add_argument("--debug", type=bool, default=False)
parser.add_argument("--debug_id", type=int, default=0)
parser.add_argument("--gpt", type=str, default="gpt3")
parser.add_argument("--prompt", type=str, default="easy")
args = parser.parse_args()
root = '{}/benchmark/ReAct/root'.format(args.path)

os.environ['api_key'] = args.api_key
if args.gpt == "gpt3":
    from agents import ReactAgent
file_path = "{}/data/qapairs.jsonl".format(args.path, args.dataset, args.hardness)
with open(file_path, 'r') as f:
    contents = []
    for item in jsonlines.Reader(f):
        contents.append(item)

if args.debug:
    random_indices = args.debug_id
    test_q = contents[random_indices]['question']
    test_a = contents[random_indices]['answer']
    agent = ReactAgent(args, test_q, test_a)
    agent.run()
    print(test_q)
    print(agent._build_agent_prompt())
    print("Ground-Truth: ", test_a)
else:
    c=  random.randint(0, 9999)
    if not os.path.exists('{}/benchmark/ReAct/logs/{}-{}-{}'.format(args.path, args.gpt, args.dataset,c)):
        os.makedirs('{}/benchmark/ReAct/logs/{}-{}-{}'.format(args.path, args.gpt, args.dataset,c))
        logs_dir = '{}/benchmark/ReAct/logs/{}-{}-{}'.format(args.path, args.gpt, args.dataset,c)
    agent_cls = ReactAgent

    n = 1
    log = ''
    trial = 0
    unanswered_questions = []
    agents = []
    final_json_output = '['
    for i in range(len(contents)):
        agent = agent_cls(args, contents[i]['question'], contents[i]['answer'], i)
        try:
            
            agent.run()
            print(f'Answer: {agent.key}')
            print('---------')
            log = f"""
########################################
BEGIN TRIAL {contents[i]['qid']}
#######################################
"""
            log += remove_fewshot(agent._build_agent_prompt()) + f'\nCorrect answer: {agent.key}\n\n'
            with open(os.path.join(logs_dir, contents[i]['qid']+'.txt'), 'w') as f:
                f.write(log)
        except Exception as e:
            print(f"An error occurred: {e}")
            print('Error when computing answer for {}.'.format(contents[i]['qid']))
            print('---------')
            log = f"""
########################################
BEGIN TRIAL {contents[i]['qid']}
#######################################
"""
            log += remove_fewshot(agent._build_agent_prompt()) + f'\nCorrect answer: {agent.key}\n\n'
            log += 'ERROR!'
            with open(os.path.join(logs_dir, contents[i]['qid']+'.txt'), 'w') as f:
                f.write(log)
            unanswered_questions.append(contents[i]['qid'])
        agent.collected_actions = agent.collected_actions[:-1] + ']},'
        final_json_output += agent.collected_actions
        agents.append(agent)
        if i == 1: 
            break # first 6 questions
    final_json_output = final_json_output[:-1] + ']'
    trial += 1
    log += log_react_trial(agents, trial)
    correct, incorrect, halted = summarize_react_trial(agents)
    print(f'Finished Trial {trial}, Correct: {len(correct)}, Incorrect: {len(incorrect)}, Halted: {len(halted)}')
    print('Unanswered questions: {}'.format(unanswered_questions))

    
    json_object = json.loads(final_json_output)

    # Now 'json_object' is a Python dictionary representing the JSON data

    json_filename = "output.json"

    # Write the dictionary to the JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(json_object, json_file, indent=2)
    # save_agents(agents, os.path.join(root, 'ReAct', 'agents'))