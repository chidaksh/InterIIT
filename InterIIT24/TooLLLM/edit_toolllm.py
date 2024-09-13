res = [
        {
          "role": "system",
          "content": "You are AutoGPT, you can use many tools(functions) to do the following task.\nFirst I will give you the task description, and your task start.\nAt each step, you need to give your thought to analyze the status now and what to do next, with a function call to actually excute your step.\nAfter the call, you will get the call result, and you are now in a new state.\nThen you will analyze your status now, then decide what to do next...\nAfter many (Thought-call) pairs, you finally perform the task, then you can give your finial answer.\nRemember: \n1.the state change is irreversible, you can't go back to one of the former state, if you want to restart the task, say \"I give up and restart\".\n2.All the thought is short, at most in 5 sentence.\n3.You can do more then one trys, so if your plan is to continusly try some conditions, you can do one of the conditions per try.\nLet's Begin!\nTask description: You should use functions to help handle the real time user querys. Remember:\n1.ALWAYS call \"Finish\" function at the end of the task. And the final answer should contain enough information to show to the user,If you can't handle the task, or you find that function calls always fail(the function is not valid now), use function Finish->give_up_and_restart.\n2.Do not use origin tool names, use only subfunctions' names.\nYou have access of the following tools:\n1.agent007: An interface to database which tracks the work items such as issues, features, bugs etc. Provides APIs to retrieve, summarize, change the database related to production cycle.\n"
        },
        {
          "role": "user",
          "content": "\nPrioritize my P0 issues and add them to the current sprint\nBegin!\n"
        },
        {
          "role": "assistant",
          "content": None,
          "function_call": {
            "name": "works_list_for_agent007",
            "arguments": "{\n  \"owned_by\": \"my\",\n  \"issue_priority\": \"p0\"\n}"
          }
        },
        {
          "role": "function",
          "name": "works_list_for_agent007",
          "content": "{\"error\": \"\", \"response\": \"['WK-001', 'WK-002']\"}"
        },
        {
          "role": "assistant",
          "content": None,
          "function_call": {
            "name": "get_sprint_id_for_agent007",
            "arguments": "{}"
          }
        },
        {
          "role": "function",
          "name": "get_sprint_id_for_agent007",
          "content": "{\"error\": \"\", \"response\": \"{'sprint_id': 'SPR-123'}\"}"
        },
        {
          "role": "assistant",
          "content": None,
          "function_call": {
            "name": "add_work_items_to_sprint_for_agent007",
            "arguments": "{\n  \"work_ids\": \"WK-001,WK-002\",\n  \"sprint_id\": \"SPR-123\"\n}"
          }
        },
        {
          "role": "function",
          "name": "add_work_items_to_sprint_for_agent007",
          "content": "{\"error\": \"\", \"response\": \"{'message': 'Work items added to sprint'}\"}"
        },
        {
          "role": "assistant",
          "content": None,
          "function_call": {
            "name": "Finish",
            "arguments": "{\n  \"return_type\": \"give_answer\",\n  \"final_answer\": \"P0 issues have been prioritized and added to the current sprint.\"\n}"
          }
        }
      ]


i = 1
txt = ""
ans = ""
for obj in res:
    # print(obj)

    if(obj['role']=="assistant"):
        # Thought
        txt += "Thought "+str(i)+": "
        if(obj['content']):
            txt += obj['content']
        txt += "\n"
        
        # Action
        txt += "Action "+str(i)+": "
        txt += obj['function_call']['name'].replace("_for_agent007", "")
        txt += "("
        txt += obj['function_call']['arguments']
        txt += ")"
        txt += "\n"
    
        if(obj['function_call']['name']=="Finish"):
            txt = ""
            txt += "Thought "+str(i)+": "
            if(obj['content']):
                txt += obj['content']
            txt += "\n"

            txt += "Action "+str(i)+": Finish()\n"

            txt += "Observation "+str(i)+": "+obj['function_call']['arguments']
            print(txt)
            ans += txt
            txt = ""

    elif(obj['role']=="function"):
        # Observation
        txt += "Observation "+str(i)+": "
        txt += "Called the function " + obj['name'].replace("_for_agent007", "") + ", observed: "
        txt += obj['content']
        txt += "\n"
        i += 1

        print(txt)
        ans += txt
        txt = ""


ans_obj = [{
    "qid": 1,
    "question": "Prioritize my P0 issues and add them to the current sprint",
    "way1": ans,
    "way2": ""
}]
with open("res.txt", "wt") as f:
    f.write(str(ans_obj))