import os
import json
import requests

class ChatGPT:
    def __init__(self):
        self.model = "chatgpt"
        self.max_tokens = 1024
        self.temperature = 0.7

    def load_api_key(self):
        #  API key from configuration
        config = [
            {
                "username": "",
                "passwd": "",
                "api_key": "",
            }
        ]
        return config[0]["api_key"]

    def prompt(self, thought, api_name, api_params, instruction, context):
        """Prompts ChatGPT to generate an action based on previous interactions."""
        api_key = self.load_api_key()
        response = requests.post(
            "https://api.openai.com/v1/completions",
            headers={
                "Authorization": "Bearer {}".format(api_key),
                "Content-Type": "application/json"
            },
            json={
                "prompt": "Thought: {}\nAPIName: {}\nParameters: {}\nInstruction: {}\nContext: {}".format(thought, api_name, api_params, instruction, context),
                "model": self.model,
                "max_tokens": self.max_tokens,
                "temperature": self.temperature
            }
        )
        response_json = json.loads(response.text)
        action = response_json["choices"][0]["text"]
        return action

class ToolLLAMA:
    def __init__(self, instructions, api_list):
        self.instructions = instructions
        self.api_list = api_list
        self.chatgpt = ChatGPT()

    def dfsdt_search(self, instruction, context):
        """Performs a depth-first search of the decision tree to find a valid solution path."""
        node_stack = [(instruction, context)]
        while node_stack:
            instruction, context = node_stack.pop()
            for api in self.api_list:
                api_name = api["name"]
                api_params = api["params"]
                action = self.chatgpt.prompt("I need to use the {} API to complete the instruction.".format(api_name), api_name, api_params, instruction, context)
                if action == "Finish withFinalAnswer":
                    return action, context
                elif action == "Finish by Giving Up":
                    continue
                else:
                    new_context = context + action
                    node_stack.append((instruction, new_context))

    def generate_solution_paths(self):
        """Generates all possible solution paths for the given instructions."""
        for instruction in self.instructions:
            action, context = self.dfsdt_search(instruction, "")
            if action == "Finish withFinalAnswer":
                solution_path = (instruction, context)
                yield solution_path

    def train_tool_llama(self):
        """Trains Tool LLAMA on the generated solution paths."""
        pass

if __name__ == "__main__":
    # Load instructions and APIs from JSON files
    with open("instructions.json") as f:
        instructions = json.load(f)
    with open("apis.json") as f:
        api_list = json.load(f)

    # Create ToolLLAMA instance
    tool_llama = ToolLLAMA(instructions, api_list)

    # Generate solution paths
    solution_paths = tool_llama.generate_solution_paths()

    # Train Tool LLAMA
    tool_llama.train_tool_llama()
