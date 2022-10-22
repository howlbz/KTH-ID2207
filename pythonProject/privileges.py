Privileges = {
    "cs": ["workflow1_add", "workflow1_send", "workflow1_search_state"],
    "scs": ["workflow1_send", "workflow1_update", "workflow1_reject", "workflow1_search_state"],
    "fm": ["workflow1_send", "workflow1_update", "workflow1_search_state"],
    "am": ["workflow1_accept", "workflow1_reject", "workflow1_search_state"],
    "sub_team": ["workflow2_plan", "workflow2_send", "workflow2_record_number", "workflow2_search_state",
                 "workflow2_comment"],
    "pm": ["workflow2_sub_team", "workflow2_task", "workflow2_send", "workflow2_record_number",
           "workflow2_search_state"]
}

workflow1_add_state = False
workflow1_send_state = False
workflow1_update_state = False
workflow1_accept_state = False
workflow1_reject_state = False
workflow1_search_state = False

workflow2_sub_team = False
workflow2_task = False
workflow2_plan = False
workflow2_send = False
workflow2_record_number = False
workflow2_search = False
workflow2_comment = False


def get_privilege(permission):
    if "workflow1_add" not in Privileges[permission]:
        global workflow1_add_state
        workflow1_add_state = True
    if "workflow1_send" not in Privileges[permission]:
        global workflow1_send_state
        workflow1_send_state = True
    if "workflow1_update" not in Privileges[permission]:
        global workflow1_update_state
        workflow1_update_state = True
    if "workflow1_accept" not in Privileges[permission]:
        global workflow1_accept_state
        workflow1_accept_state = True
    if "workflow1_reject" not in Privileges[permission]:
        global workflow1_reject_state
        workflow1_reject_state = True
    if "workflow1_search_state" not in Privileges[permission]:
        global workflow1_search_state
        workflow1_search_state = True

    if "workflow2_sub_team" not in Privileges[permission]:
        global workflow2_sub_team
        workflow2_sub_team = True
    if "workflow2_task" not in Privileges[permission]:
        global workflow2_task
        workflow2_task = True
    if "workflow2_plan" not in Privileges[permission]:
        global workflow2_plan
        workflow2_plan = True
    if "workflow2_send" not in Privileges[permission]:
        global workflow2_send
        workflow2_send = True
    if "workflow2_record_number" not in Privileges[permission]:
        global workflow2_record_number
        workflow2_record_number = True
    if "workflow2_search_state" not in Privileges[permission]:
        global workflow2_search
        workflow2_search = True
    if "workflow2_comment" not in Privileges[permission]:
        global workflow2_comment
        workflow2_comment = True
