from langchain.prompts import PromptTemplate

REACT_INSTRUCTION_ = """Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be 13 types: 
(1) Calculate[formula], which calculates the formula and returns the result.
(2) RetrieveAgenda[keyword], which retrieves the agenda related to keyword.
(3) RetrieveScirex[keyword], which retrieves machine learning papers' paragraphs related to keyword.
(4) LoadDB[DBName], which loads the database DBName and returns the database. The DBName can be one of the following: flights/coffee/airbnb/yelp.
(5) FilterDB[condition], which filters the database DBName by the column column_name the relation (e.g., =, >, etc.) and the value value, and returns the filtered database.
(6) GetValue[column_name], which returns the value of the column column_name in the database DBName.
(7) LoadGraph[GraphName], which loads the graph GraphName and returns the graph. The GraphName can be one of the following: PaperNet/AuthorNet.
(8) NeighbourCheck[GraphName, Node], which lists the neighbours of the node Node in the graph GraphName and returns the neighbours. 
(9) NodeCheck[GraphName, Node], which returns the detailed attribute information of Node. 
(10) EdgeCheck[GraphName, Node1, Node2], which returns the detailed attribute information of the edge between Node1 and Node2. 
(11) SQLInterpreter[SQL], which interprets the SQL query SQL and returns the result.
(12) PythonInterpreter[Python], which interprets the Python code Python and returns the result.
(13) Finish[answer], which returns the answer and finishes the task.
You may take as many steps as necessary.
Here are some examples:
{examples}
(END OF EXAMPLES)
# Question: {question}{scratchpad}"""

REACT_INSTRUCTION = """
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be 11 types:
Here is a mock database of work items
(1)filter_work_items(**filters),This function filters work items based on specified criteria by iterating through the provided filters and selecting items that match the specified key-value pairs or include the specified values in the key's list, returning the filtered items.
(2)works_list(applies_to_part = None), Filters for work belonging to any of the provided parts, Argument type is an array of strings, Example: ["FEAT-123","ENH-123","PROD-123","CAPL-123"]
(3)works_list(created_by = None),Filters for work created by any of these users, Argument type is an array of strings, Example: ["DEVU-123"]
(4)works_list(issue.priority = None), Filters for issues with any of the provided priorities. Allowed values: p0, p1, p2, p3, Argument type is an array of strings
(5)works_list(issue.rev_orgs = None), Filters for issues with any of the provided Rev organizations, Argument type is an array of strings, Example: ["REV-123"]
(6)works_list(limit = None), The maximum number of works to return. The default is '50', Argument type is integer (int32)
(7)works_list(owned_by = None), Filters for work owned by any of these users, Argument type is an array of strings, Example: ["DEVU-123"]
(8)works_list(stage.name = None), Filters for records in the provided stage(s) by name, Argument type is an array of strings
(9)works_list(ticket.needs_response = None), Filters for tickets that need a response, Argument type is boolean
(10)works_list(ticket.rev_org = None), Filters for tickets associated with any of the provided Rev, Argument type is an array of strings, Example: ["REV-123"]
(11)works_list(ticket.severity = None), Filters for tickets with any of the provided severities. Allowed values: blocker, high, low, medium, Argument type is an array of strings
(12)works_list(ticket.source_channel = None), Filters for tickets with any of the provided source channels, Argument type is an array of strings
(13)works_list(type = None), Filters for work of the provided types. Allowed values: issue, ticket, task, Argument type is an array of strings
(14)summarize_objects(objects = None),Summarizes a list of objects.
(15)prioritize_objects(objects = None),Returns a list of objects sorted by priority.
(16)add_work_items_to_sprint(work_ids = None, sprint_id = None),Adds the list of work item IDs to the sprint_id provided.
(17)get_sprint_id(),Returns a mock ID of the current sprint.
(18)get_similar_work_items(work_id = None),Returns a list of work items that are similar to the given work item.
(19)search_object_by_name(query = None),Given a search string, returns the id of a matching object in the system of record.
(20)create_actionable_tasks_from_text(text = None),Given a text, extracts mock actionable insights, and creates tasks for them.
(21)who_am_i(),Returns a mock string ID of the current user.
(22)average_priority(objects = None),Returns the average priority of a list of objects.
(23)select_first_k_tasks(objects = None),Returns the first k tasks from a list of objects.
(24)select_last_k_tasks(objects = None),Returns the last k tasks from a list of objects.
(25)compare_priorities(object1 = None, object2 = None),Compares the priorities of two objects and returns the higher priority object.
(26)count_tasks(objects = None),Counts the number of tasks in a list of objects.
(27) Finish[answer], which returns the answer in json format and finishes the task. 
You may take as many steps as necessary.
Here are some examples:
{examples}
(END OF EXAMPLES)
Question: {question}{scratchpad}
"""

REACT_REFLECT_INSTRUCTION = """Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be 13 types: 
(1) Calculate[formula], which calculates the formula and returns the result.
(2) RetrieveAgenda[keyword], which retrieves the agenda containing keyword and returns the agenda.
(3) RetrieveScirex[keyword], which retrieves the most relevant paragraphs in machine learning-related papers to keyword and returns the paragraphs.
(4) LoadDB[DBName], which loads the database DBName and returns the database. The DBName can be one of the following: flights/coffee/airbnb/yelp.
(5) FilterDB[condition], which filters the database DBName by the column column_name the relation (e.g., =, >, etc.) and the value value, and returns the filtered database.
(6) GetValue[column_name], which returns the value of the column column_name in the database DBName.
(7) LoadGraph[GraphName], which loads the graph GraphName and returns the graph. The GraphName can be one of the following: PaperNet/AuthorNet.
(8) NeighbourCheck[GraphName, Node], which lists the neighbours of the node Node in the graph GraphName and returns the neighbours. 
(9) NodeCheck[GraphName, Node], which returns the detailed attribute information of Node. 
(10) EdgeCheck[GraphName, Node1, Node2], which returns the detailed attribute information of the edge between Node1 and Node2. 
(11) SQLInterpreter[SQL], which interprets the SQL query SQL and returns the result.
(12) PythonInterpreter[Python], which interprets the Python code Python and returns the result.
(13) Finish[answer], which returns the answer and finishes the task.
You may take as many steps as necessary.
Here are some examples:
{examples}
(END OF EXAMPLES)

{reflections}

Question: {question}{scratchpad}"""

REFLECTION_HEADER = 'You have attempted to answer following question before and failed. The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.\n'
LAST_TRIAL_HEADER = 'You have attempted to answer the following question before and failed. Below is the last trial you attempted to answer the question.\n'



react_agent_prompt = PromptTemplate(
                        input_variables=["examples", "question", "scratchpad"],
                        template = REACT_INSTRUCTION,
                        )