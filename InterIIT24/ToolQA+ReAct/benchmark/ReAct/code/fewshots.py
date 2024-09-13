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
Action 4:Finish[" "]

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
Action 6: Finish[" "]

Question: What is the meaning of life?
Thought 1: This is a question related to meaning of life.
Action 1: Finish[ "[]" ]

Question: What are my all issues in the triage stage under part FEAT-123? Summarize them.
Thought 1: This is a question related to summarizing all issues in the triage stage under part FEAT-123.
Action 1: Response["{\"tool_name\": \"whoami\", \"arguments\": []}"]
Observation 1: Called the function whoami.
Thought 2: We need to obtain the work list of items in the triage stage under part FEAT-123 of the above obtained object.
Action 2: Response["{\"tool_name\": \"works_list\", \"arguments\": [{\"argument_name\": \"stage.name\", \"argument_value\": \"triage\"}, {\"argument_name\": \"applies_to_part\", \"argument_value\": \"FEAT-123\"}, {\"argument_name\": \"owned_by\", \"argument_value\": \"$$PREV[0]\"}]}"]
Observation 2: Called works_list with the results obtained from whoami to get items in the triage stage, applies to part FEAT-123, and are owned by the object returned by whoami[].
Thought 3: We need to summarize the above obtained work list.
Action 3: Response["{\"tool_name\": \"summarize_objects\", \"arguments\": [{\"argument_name\": \"objects\", \"argument_value\": \"$$PREV[1]\"}]}"]
Observation 3: Called summarize_objects with the result obtained from works_list.
Thought 4: After this, we have summarized all issues in the triage stage under part FEAT-123 of a given customer.
Action 4: Finish[" "]

Question: List all high severity tickets coming in from Slack from customer Cust123 and generate a summary of them.
Thought 1: This is a question related to listing all high severity tickets coming in from Slack from customer Cust123 and generating a summary of them.
Action 1: Response["{\"tool_name\": \"search_object_by_name\", \"arguments\": [{\"argument_name\": \"query\", \"argument_value\": \"Cust123\"}]}"]
Observation 1: Called the function search_object_by_name and obtained the object of Cust123.
Thought 2: We need to obtain the work list of the above customer, where items are of high severity and the source is Slack.
Action 2: Response["{\"tool_name\": \"works_list\", \"arguments\": [{\"argument_name\": \"ticket.rev_org\", \"argument_value\": \"$$PREV[0]\"}, {\"argument_name\": \"ticket.severity\", \"argument_value\": \"high\"}, {\"argument_name\": \"ticket.source_channel\", \"argument_value\": \"slack\"}]}"]
Observation 2: Called works_list and obtained items of Cust123 which have high severity and whose source is Slack.
Thought 3: We need to summarize the above obtained work list.
Action 3: Response["{\"tool_name\": \"summarize_objects\", \"arguments\": [{\"argument_name\": \"objects\", \"argument_value\": \"$$PREV[1]\"}]}"]
Observation 3: Called summarize_objects with the result obtained from works_list.
Thought 4: After this, we have summarized all high severity tickets coming in from Slack from customer Cust123.
Action 4: Finish[" "]

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
Action 4: Finish[" "]

Question: Get all work items similar to TKT-123, summarize them, create issues from that summary, and prioritize them
Thought 1: Get all similar work items to TKT-123.
Action 1: Response["{\"tool_name\": \"get_similar_work_items\", \"arguments\": [{\"argument_name\": \"work_id\", \"argument_value\": \"TKT-123\"}]}"]
Observation 1: Similar work items to TKT-123 have been fetched.
Thought 2: Summarize the objects that have been fetched in the above query response.
Action 2: Response["{\"tool_name\": \"summarize_objects\", \"arguments\": [{\"argument_name\": \"objects\", \"argument_value\": \"$$PREV[0]\"}]}"]
Observation 2: All the objects have been summarized.
Thought 3: Create actionable tasks from the summary received above.
Action 3: Response["{\"tool_name\": \"create_actionable_tasks_from_text\", \"arguments\": [{\"argument_name\": \"text\", \"argument_value\": \"$$PREV[1]\"}]}"]
Observation 3: All tasks have been created from the above summaries.
Thought 4: Prioritize the objects which have issues listed in the above actions corresponding to the summary.
Action 4: Response["{\"tool_name\": \"prioritize_objects\", \"arguments\": [{\"argument_name\": \"objects\", \"argument_value\": \"$$PREV[2]\"}]}"]
Observation 4: Objects with issues have been prioritized.
Thought 5: After this, we have obtained all work items similar to TKT-123, summarized them, created issues from that summary, and prioritized them.
Action 5: Finish[" "]

Question: Get the list of similar work items for the work id = 12 and list issues similar to user/78 also tell about what is life?
Thought 1: Get all similar work items for work id 12.
Action 1: Response["{\"tool_name\": \"get_similar_work_items\", \"arguments\": [{\"argument_name\": \"work_id\", \"argument_value\": \"12\"}]}"]
Observation 1: Called the function get_similar_work_items and obtained similar work items.
Thought 2: List issues similar to user/78.
Action 2: Response["{\"tool_name\": \"get_similar_work_items\", \"arguments\": [{\"argument_name\": \"work_id\", \"argument_value\": \"user/78\"}]}"]
Observation 2: Called the function get_similar_work_items and obtained similar work items.
Thought 3: This is a question related to the meaning of life.
Action 3: Finish[" "]

Question: Count the number of tasks in the current sprint.
Thought 1: Get the sprint id.
Action 1: Response["{\"tool_name\": \"get_sprint_id\", \"arguments\": []}"]
Observation 1: Called get_sprint_id to obtain the current sprint id.
Thought 2: Obtain the work list for the current sprint.
Action 2: Response["{\"tool_name\": \"works_list\", \"arguments\": [{\"argument_name\": \"sprint_id\", \"argument_value\": \"$$PREV[0]\"}]}"]
Observation 2: Called works_list and obtained the work list for the current sprint.
Thought 3: Count the number of tasks in the current sprint.
Action 3: Response["{\"tool_name\": \"count_tasks\", \"arguments\": [{\"argument_name\": \"objects\", \"argument_value\": \"$$PREV[1]\"}]}"]
Observation 3: Counted the number of tasks in the current sprint.
Action 4: Finish[" "]
"""
