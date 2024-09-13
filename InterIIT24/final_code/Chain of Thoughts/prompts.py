TOOL_DESCRIPTION = f"""
(1) filter_work_items(**filters),
    This function filters work items based on specified criteria by iterating through the provided filters and selecting items that match the specified key-value pairs or include the specified values in the key's list, returning the filtered items.

(2) works_list(applies_to_part=None),
    Filters for work belonging to any of the provided parts, Argument type is an array of strings, Example: ["FEAT-123","ENH-123","PROD-123","CAPL-123"]

(3) works_list(created_by=None),
    Filters for work created by any of these users, Argument type is an array of strings, Example: ["DEVU-123"]

(4) works_list(issue.priority=None),
    Filters for issues with any of the provided priorities. Allowed values: p0, p1, p2, p3, Argument type is an array of strings

(5) works_list(issue.rev_orgs=None),
    Filters for issues with any of the provided Rev organizations, Argument type is an array of strings, Example: ["REV-123"]

(6) works_list(limit=None),
    The maximum number of works to return. The default is '50', Argument type is integer (int32)

(7) works_list(owned_by=None),
    Filters for work owned by any of these users, Argument type is an array of strings, Example: ["DEVU-123"]

(8) works_list(stage.name=None),
    Filters for records in the provided stage(s) by name, Argument type is an array of strings

(9) works_list(ticket.needs_response=None),
    Filters for tickets that need a response, Argument type is boolean

(10) works_list(ticket.rev_org=None),
    Filters for tickets associated with any of the provided Rev, Argument type is an array of strings, Example: ["REV-123"]

(11) works_list(ticket.severity=None),
    Filters for tickets with any of the provided severities. Allowed values: blocker, high, low, medium, Argument type is an array of strings

(12) works_list(ticket.source_channel=None),
    Filters for tickets with any of the provided source channels, Argument type is an array of strings

(13) works_list(type=None),
    Filters for work of the provided types. Allowed values: issue, ticket, task, Argument type is an array of strings

(14) summarize_objects(objects=None),
    Summarizes a list of objects.

(15) prioritize_objects(objects=None),
    Returns a list of objects sorted by priority.

(16) add_work_items_to_sprint(work_ids=None, sprint_id=None),
    Adds the list of work item IDs to the sprint_id provided.

(17) get_sprint_id(),
    Returns a mock ID of the current sprint.

(18) get_similar_work_items(work_id=None),
    Returns a list of work items that are similar to the given work item.

(19) search_object_by_name(query=None),
    Given a search string, returns the id of a matching object in the system of record. If multiple matches are found, it returns the one where the confidence is highest. Argument name: query, description: The search string, could be for example customer's name, part name, user name.

(20) create_actionable_tasks_from_text(text=None),
    Given a text, extracts mock actionable insights, and creates tasks for them.

(21) who_am_i(),
    Returns a mock string ID of the current user.

(22) average_priority(objects=None),
    Returns the average priority of a list of objects.

(23) select_first_k_tasks(objects=None),
    Returns the first k tasks from a list of objects.

(24) select_last_k_tasks(objects=None),
    Returns the last k tasks from a list of objects.

(25) compare_priorities(object1=None, object2=None),
    Compares the priorities of two objects and returns the higher priority object.
"""


EXAMPLE1 = f"""<Example1>
Question: Prioritize my P0 issues and add them to the current sprint
Thoughts: Chain of thoughts: Identify me with "whoami" -> Identify P0 Issues using "works_list" tool -> Prioritize P0 Issues using "prioritize_objects" tool -> Get the current Sprint ID using "get_sprint_id" -> Add prioritized issues to the current Sprint using "add_work_items_to_sprint" tool.
<Output>
 "answer": [
    {{
        "tool_name": "whoami",
        "arguments": []
    }},
    {{
        "tool_name": "works_list",
        "arguments": [
            {{
                "argument_name": "issue.priority",
                "argument_value": ["p0"]
            }},
            {{
                "argument_name": "owned_by",
                "argument_value": ["$$PREV[0]"]
            }},
            {{
                "argument_name": "type",
                "argument_value": ["issue"]
            }}
        ]
    }},
    {{
        "tool_name": "prioritize_objects",
        "arguments": [
            {{
                "argument_name": "objects",
                "argument_value": "$$PREV[1]"
            }}
        ]
    }},
    {{
        "tool_name": "get_sprint_id",
        "arguments": []
    }},
    {{
        "tool_name": "add_work_items_to_sprint",
        "arguments": [
            {{
                "argument_name": "work_ids",
                "argument_value": "$$PREV[2]"
            }},
            {{
                "argument_name": "sprint_id",
                "argument_value": "$$PREV[3]"
            }}
        ]
    }}
] 
</Output> 
</Example1>"""


EXAMPLE2 = f"""<Example2>
Question: Given a customer meeting transcript T, create action items and add them to my current sprint
Thoughts: Chain of thoughts: Create Actionable Tasks from Text using "create_actionable_tasks_from_text" tool -> Get the current Sprint ID using "get_sprint_id" tool -> Add Actionable Tasks to the Current Sprint using "add_work_items_to_sprint" tool

<Output>
 "answer": [
    {{
        "tool_name": "create_actionable_tasks_from_text",
        "arguments": [
            {{
                "argument_name": "text",
                "argument_value": "T"
            }}
        ]
    }},
    {{
        "tool_name": "get_sprint_id",
        "arguments": []
    }},
    {{
        "tool_name": "add_work_items_to_sprint",
        "arguments": [
            {{
                "argument_name": "work_ids",
                "argument_value": "$$PREV[0]"
            }},
            {{
                "argument_name": "sprint_id",
                "argument_value": "$$PREV[1]"
            }}
        ]
    }}
] 
</Output>
</Example2>"""

EXAMPLE3 = f"""<Example3>
Question: Summarize high severity tickets from the customer UltimateCustomer
Thoughts: Chain of thoughts: Search for the customer using "search_object_by_name" tool -> Filter high severity tickets for the customer using "works_list" tool -> Summarize the high severity tickets using "summarize_objects" tool

<Output>
 "answer": [
    {{
        "tool_name": "search_object_by_name",
        "arguments": [
            {{ "argument_name": "query", "argument_value": "UltimateCustomer" }}
        ]
    }},
    {{
        "tool_name": "works_list",
        "arguments": [
            {{ "argument_name": "ticket.rev_org", "argument_value": ["$$PREV[0]"] }},
            {{ "argument_name": "ticket.severity", "argument_value": ["high"] }},
            {{ "argument_name": "type", "argument_value": ["ticket"] }}
        ]
    }},
    {{
        "tool_name": "summarize_objects",
        "arguments": [
            {{ "argument_name": "objects", "argument_value": "$$PREV[1]" }}
        ]
    }}
] 
</Output>
</Example3>"""


PROMPT_TEMPLATE = f"""Your task is to Output the json format of tools and arguments for a given question using the tools and required arguments provided below.
1. Follow the examples in the methodology given
2. Please output only "answer" and nothing else.
3. You must use whom_am_i tool only when "my" appears in the question.
4. If the question is not answerable then output "answer": "[]" in JSON format.
5. You must use given tools only, do not assume any other new function.

<Functions>
These are the only tools you are provided with.
{TOOL_DESCRIPTION}
(26) count_tasks(objects=None), Counts the number of tasks in a list of objects.
</Functions>

<Methodology>
To answer a given question, you have to develop a chain of thought to give the answer.
{EXAMPLE1}
{EXAMPLE2}
{EXAMPLE3}
</Methodology>

USE ONLY GIVEN TOOLS. DO NOT ASSUME NEW TOOLS.
Do not output anything other than "answer" in PROPER JSON format.If the question is not answerable then output "answer": "[]" in JSON format.

Answer this question ::
Question :: 
"""

    