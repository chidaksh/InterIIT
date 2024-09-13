class WorkItem:
    def __init__(self, id, applies_to_part, created_by, issue_priority, issue_rev_orgs, owned_by,
                 stage_name, ticket_needs_response, ticket_rev_org, ticket_severity,
                 ticket_source_channel, work_item_type):
        self.id = id
        self.applies_to_part = applies_to_part
        self.created_by = created_by
        self.issue_priority = issue_priority
        self.issue_rev_orgs = issue_rev_orgs
        self.owned_by = owned_by
        self.stage_name = stage_name
        self.ticket_needs_response = ticket_needs_response
        self.ticket_rev_org = ticket_rev_org
        self.ticket_severity = ticket_severity
        self.ticket_source_channel = ticket_source_channel
        self.type = work_item_type

    def summarize(self):
        summary = f"Work Item ID: {self.id}\n"
        summary += f"Created By: {self.created_by}\n"
        summary += f"Owned By: {self.owned_by}\n"
        summary += f"Stage: {self.stage_name}\n"
        summary += f"Priority: {self.issue_priority}\n"
        summary += f"Severity: {self.ticket_severity}\n"
        summary += f"Source Channel: {self.ticket_source_channel}\n"
        summary += f"Needs Response: {'Yes' if self.ticket_needs_response else 'No'}\n"
        summary += f"Type: {self.type}\n"
        summary += f"Applies to Parts: {', '.join(self.applies_to_part)}\n"
        summary += f"Issue Rev Orgs: {', '.join(self.issue_rev_orgs)}\n"
        summary += f"Ticket Rev Org: {self.ticket_rev_org}\n"

        return summary

    def get(self, attr):
        return self.__getattribute__(attr)




work_items = [
	{
        "id": "WK-001",
        "applies_to_part": ["FEAT-123", "ENH-123"],
        "created_by": "USER-123",
        "issue_priority": "p0",
        "issue_rev_orgs": ["REV-001"],
        "owned_by": "USER-456",
        "stage_name": "development",
        "ticket_needs_response": True,
        "ticket_rev_org": "REV-002",
        "ticket_severity": "high",
        "ticket_source_channel": "email",
        "work_item_type": "issue"
    },
    {
        "id": "WK-002",
        "applies_to_part": ["FEAT-124", "ENH-121"],
        "created_by": "USER-456",
        "issue_priority": "p0",
        "issue_rev_orgs": ["REV-001"],
        "owned_by": "USER-456",
        "stage_name": "development",
        "ticket_needs_response": True,
        "ticket_rev_org": "REV-002",
        "ticket_severity": "low",
        "ticket_source_channel": "email",
        "work_item_type": "issue"
    },
    {
        "id": "WK-003",
        "applies_to_part": ["FEAT-123", "ENH-123"],
        "created_by": "USER-123",
        "issue_priority": "p1",
        "issue_rev_orgs": ["REV-001"],
        "owned_by": "USER-454",
        "stage_name": "development",
        "ticket_needs_response": True,
        "ticket_rev_org": "REV-002",
        "ticket_severity": "high",
        "ticket_source_channel": "email",
        "work_item_type": "feature"
    }
]

work_items_db = [WorkItem(**i) for i in work_items]

def filter_work_items(**filters):
    filtered_items = work_items_db
    out = []
    for key, value in filters.items():
        if value is not None:
            out = out + [item.id for item in filtered_items if item.get(key) == value or value in item.get(key)]
    return out

def works_list(**kwargs):
    """
        Returns a list of work items matching the request.
        arguements can be as follows. The work item for which all the parameters of 
        request are matched is returned.
        id:
        applies_to_part": 
        created_by: 
        issue_priority: 
        issue_rev_orgs": 
        owned_by: 
        stage_name: 
        ticket_needs_response": 
        ticket_rev_org: 
        ticket_severity: 
        ticket_source_channel: 
        type: 
    """
    return filter_work_items(**kwargs)

# need to convert the object type from str to proper datatype
def summarize_work_items(objects: WorkItem = None):
    """Summarizes a list of work items."""
    try: 
        summarized = []
        for obj in objects:
            summarized.append(obj.summarize())
    except:
        return {"error": "Not a valid object. Please give list of WorkItem objects as arguement"}    
    return summarized
    

def prioritize_objects(objects = None):
    """Returns a list of objects sorted by priority."""
    # This is a mock prioritization logic based on issue_priority
    print(objects, type(objects))
    if objects is None:
        return
    if objects == "P0":
        return {"error": "Not a valid object. Please get the objects using works_list"}
    else:
        priority_map = {'p0': 1, 'p1': 2, 'p2': 3, 'p3': 4}
        return sorted(objects)
        # return sorted(objects, key=lambda x: priority_map.get(x['issue_priority'], 5))

def add_work_items_to_sprint(work_ids = None, sprint_id = None):
    """Adds the given work items to the sprint."""
    # Mock logic to update the 'sprint_id' for each work item
    if sprint_id == "":
        return {"error:": "No sprint id or work id given"}
    else:
        for work_item in work_items_db:
            if work_item.id in work_ids:
                work_item.sprint_id = sprint_id
        return {"message": "Work items added to sprint"}

def get_sprint_id():
    """Returns a mock ID of the current sprint."""
    return {"sprint_id": "SPR-123"}

def get_similar_work_items(work_id = None):
    """Returns a list of work items that are similar to the given work item."""
    # This is a mock similarity logic based on 'type'
    return ['don:core:dvrv-us-1:devo/0:issue/2', 'don:cpu:dvrv-us-1:devo/0:issue/1']
    if work_id is None:
        return
    else:
        # reference_item = next((item for item in work_items_db if item['id'] == work_id), None)
        # if not reference_item:
        #     return []
        # similar_items = [item for item in work_items_db if item['type'] == reference_item['type']]
        similar_items = [work_items_db[0]]
        return similar_items

def search_object_by_name(query = None):
    """Given a search string, returns the id of a matching object in the system of record."""
    # Mock search logic
    if query is None:
        return
    else:
        search_results = [item for item in work_items_db if query in item.values()]
        if not search_results:
            return None
        return search_results[0]['id']  # Return the ID of the first match

def create_actionable_tasks_from_text(text = None):
    """Given a text, extracts mock actionable insights, and creates tasks for them."""
    # Mock logic to create a task from text
    if text is None:
        return
    else:
        new_task = {"id": "TASK-001", "text": text, "type": "task"}
        work_items_db.append(new_task)
        return new_task

def who_am_i():
    """Returns a mock string ID of the current user."""
    return {"user_id": "USER-123"}


# print(who_am_i())
# if __name__=="__main__":
#     out = works_list(**{
#                     "owned_by": "USER-123",
#                     "issue_priority": "p0"
#                     })
#     print([i.summarize() for i in out])