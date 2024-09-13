import re
import json

# # Your provided JSON
# json_data = [
#   {
#     "tool_name": "get_similar_work_items_for_agent007",
#     "arguments": [
#       {
#         "argument_name": "work_id",
#         "argument_value": "WK-001"
#       }
#     ]
#   },
#   {
#     "tool_name": "summarize_objects_for_agent007",
#     "arguments": [
#       {
#         "argument_name": "objects",
#         "argument_value": "$$PREV[1].response"
#       }
#     ]
#   },
#   {
#     "tool_name": "summarize_objects_for_agent007",
#     "arguments": [
#       {
#         "argument_name": "objects",
#         "argument_value": "WK-001"
#       }
#     ]
#   },
#   {
#     "tool_name": "summarize_objects_for_agent007",
#     "arguments": [
#       {
#         "argument_name": "objects",
#         "argument_value": "WK-002"
#       }
#     ]
#   },
#   {
#     "tool_name": "summarize_objects_for_agent007",
#     "arguments": [
#       {
#         "argument_name": "objects",
#         "argument_value": "WK-001,WK-002"
#       }
#     ]
#   },
#   {
#     "tool_name": "Finish",
#     "arguments": [
#       {
#         "argument_name": "return_type",
#         "argument_value": "give_answer"
#       },
#       {
#         "argument_name": "final_answer",
#         "argument_value": "There are 2 issues similar to WK-001: WK-001 and WK-002.\n\n- Issue WK-001:\n  - Created By: USER-123\n  - Owned By: USER-456\n  - Stage: development\n  - Priority: p0\n  - Severity: high\n  - Source Channel: email\n  - Needs Response: Yes\n  - Type: issue\n  - Applies to Parts: FEAT-123, ENH-123\n  - Issue Rev Orgs: REV-001\n  - Ticket Rev Org: REV-002\n\n- Issue WK-002:\n  - Created By: USER-456\n  - Owned By: USER-456\n  - Stage: development\n  - Priority: p0\n  - Severity: low\n  - Source Channel: email\n  - Needs Response: Yes\n  - Type: issue\n  - Applies to Parts: FEAT-124, ENH-121\n  - Issue Rev Orgs: REV-001\n  - Ticket Rev Org: REV-002\n\nPlease let me know if you need more information about these issues or if there's anything specific you would like to do with them."
#       }
#     ]
#   }
# ]



# # Function to remove trailing part after $$PREV[i] until a "

# # Convert the JSON data to a string
# json_string = json.dumps(json_data)

# # Use regular expressions to remove trailing part after $$PREV[i]
# pattern = re.compile(r'\$\$PREV\[(\d+)\]([^"]*?)')
# json_string_modified = pattern.sub(replace_match, json_string)

# print(json_string_modified)
# # Convert the modified string back to JSON
# json_data_modified = json.loads(json_string_modified)

# # Print the resulting JSON object
# print(json.dumps(json_data_modified, indent=2))

def replace_match(match):
        # Extract the integer value and reconstruct the replacement string
        index = match.group(1)
        print(match)
        print(index)
        replacement = f'$$PREV[{index}]'
        return replacement
str = '"$$PREV[1].response"'
pattern = re.compile(r'\$\$PREV\[(\d+)\][^"]*')
json_string_modified = pattern.sub(replace_match, str)

print(json_string_modified)