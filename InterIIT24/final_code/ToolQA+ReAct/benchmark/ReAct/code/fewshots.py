TOOLQA_EASY8 = """
Question: Summarize high severity tickets from the customer UltimateCustomer
Thought 1: This is a question related to summarizing high severity tickets from the customer UltimateCustomer.
Action 1: Response["{\"tool_name\": \"search_object_by_name\", \"arguments\": [{\"argument_name\": \"query\", \"argument_value\": \"UltimateCustomer\"}]}"]
Observation 1: Called the function search_object_by_name and obtained the object of UltimateCustomer.
Thought 2: We need to obtain the high severity work list of the above obtained object.
Action 2: Response["{\"tool_name\": \"works_list\", \"arguments\": [{\"argument_name\": \"ticket.rev_org\", \"argument_value\": \"$$PREV[0]\"}]}"]
Observation 2: We have called works_list and obtained tickets of the object (customer) UltimateCustomer.
Thought 3: We need to summarize the obtained work list.
Action 3: Response["{\"tool_name\": \"summarize_objects\", \"arguments\": [{\"argument_name\": \"objects\", \"argument_value\": \"$$PREV[1]\"}]}"]
Observation 3: We have called summarize_objects with the result obtained from works_list.
Thought 4: After this, we have summarized the high severity tickets from the customer UltimateCustomer.
Action 4:Finish[""]

Question: What is the meaning of life?
Thought 1: This is a question related to meaning of life.
Action 1: Finish[ "[]" ]

Question: Prioritize my P0 issues and add them to the current sprint
Thought 1: This is a question related to prioritizing P0 issues and adding them to the current sprint.
Action 1: Response["{\"tool_name\": \"whoami\", \"arguments\": []}"]
Observation 1: Called the function whoami.
Thought 2: We need to obtain the work list with priority issues, owned_by, and type.
Action 2: Response["{\"tool_name\": \"works_list\", \"arguments\": [{\"argument_name\": \"issue.priority\", \"argument_value\": \"p0\"}, {\"argument_name\": \"owned_by\", \"argument_value\": \"$$PREV[0]\"}, {\"argument_name\": \"type\", \"argument_value\": \"issue\"}]}"]
Observation 2: Called works_list with results obtained from whoami to get priority issues, owned_by, and type.
Thought 3: We need to obtain priority objects.
Action 3: Response["{\"tool_name\": \"prioritize_objects\", \"arguments\": [{\"argument_name\": \"objects\", \"argument_value\": \"$$PREV[1]\"}]}"]
Observation 3: Called prioritize_objects with the result obtained from works_list to get priority objects.
Thought 4: We need to get the sprint id.
Action 4: Response["{\"tool_name\": \"get_sprint_id\", \"arguments\": []}"]
Observation 4: Called get_sprint_id.
Thought 5: We need to add work items to the sprint.
Action 5: Response["{\"tool_name\": \"add_work_items_to_sprint\", \"arguments\": [{\"argument_name\": \"work_ids\", \"argument_value\": \"$$PREV[2]\"}, {\"argument_name\": \"sprint_id\", \"argument_value\": \"$$PREV[3]\"}]}"]
Observation 5: Called add_work_items_to_sprint with the results obtained from get_sprint_id.
Thought 6: After this, we have prioritized the P0 issues and added them to the current sprint.
Action 6: Finish[""]

Question: Given a customer meeting transcript T, create action items and add them to my current sprint
Thought 1: Create all actions deciphered from the text in the transcript.
Action 1: Response["{\"tool_name\": \"create_actionable_tasks_from_text\", \"arguments\": [{\"argument_name\": \"text\", \"argument_value\": \"T\"}]}"]
Observation 1: All actions are created which can be understood from the transcript.
Thought 2: Get my sprint to add the current actions.
Action 2: Response["{\"tool_name\": \"get_sprint_id\", \"arguments\": []}"]
Observation 2: Current sprint_id has been fetched.
Thought 3: Add our current actions to our sprint.
Action 3: Response["{\"tool_name\": \"add_work_items_to_sprint\", \"arguments\": [{\"argument_name\": \"work_ids\", \"argument_value\": \"$$PREV[0]\"}, {\"argument_name\": \"sprint_id\", \"argument_value\": \"$$PREV[1]\"}]}"]
Observation 3: All the actions have been added to our sprint from the transcript.
Thought 4: After this, we have created action items and added them to our current sprint.
Action 4: Finish[""]
"""
