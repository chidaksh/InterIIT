


FORMAT_INSTRUCTIONS_SYSTEM_FUNCTION = """You are AutoGPT, you can use many tools(functions) to do the following task.
First I will give you the task description, and your task start.
At each step, you need to give your thought to analyze the status now and what to do next, with a function call to actually excute your step.
After the call, you will get the call result, and you are now in a new state.
Then you will analyze your status now, then decide what to do next...
After many (Thought-call) pairs, you finally perform the task, then you can give your finial answer.
Remember: 
1.the state change is irreversible, you can't go back to one of the former state, if you want to restart the task, say "I give up and restart".
2.All the thought is short, at most in 5 sentence.
3.You can do more then one trys, so if your plan is to continusly try some conditions, you can do one of the conditions per try.
Let's Begin!
Task description: {task_description}"""

CONVERT_TO_DEVREV_PROMPT = """Convert the following output into the following format.

The format can be described as follows:
1. You should only tell the function calls that are made. In the following format. 
{
"tool_name": <function_name>,
"arguments": <List of arguments in json format>
}
example: {
    "tool_name": "prioritize_objects",
    "arguments": [
    {
    "argument_name": "objects",
    "argument_value": "$$PREV[1]"
    }
    ]
}

Here $$PREV[1] means the following:
Each output from the function call should be stored in a array called prev. 
If we are using a previous output as an argument to the function, It should be referenced by the index in the previous array. If we are using 4th Object in the prev array, we should write $$PREV[3] since the array is 0 indexed.
3. All argument values must have the $$PREV[*] format.
4. Arguments must be a list strcitly following the given format as above.
5. All of it in a single output
6. It should be in a JSON format. Separate the JSON objects by a comma.
 """

FORMAT_INSTRUCTIONS_USER_FUNCTION = """
{input_description}
Begin!
"""

FORMAT_INSTRUCTIONS_SYSTEM_FUNCTION_ZEROSHOT = """Answer the following questions as best you can. Specifically, you have access to the following APIs:

{func_str}

Use the following format:
Thought: you should always think about what to do
Action: the action to take, should be one of {func_list}
Action Input: the input to the action
End Action

Begin! Remember: (1) Follow the format, i.e,
Thought:
Action:
Action Input:
End Action
(2)The Action: MUST be one of the following:{func_list}
(3)If you believe that you have obtained enough information (which can be judge from the history observations) that can answer the task, please call:
Action: Finish
Action Input: {{"return_type": "give_answer", "final_answer": your answer string}}.
Question: {question}

Here are the history actions and observations:
"""
        