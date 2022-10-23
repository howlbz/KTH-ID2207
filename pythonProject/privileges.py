Privileges = {
    "cs": ["workflow1_add", "workflow1_send", "workflow1_search_state"],
    "scs": ["workflow1_send", "workflow1_update", "workflow1_reject", "workflow1_search_state"],
    "fm": ["workflow1_send", "workflow1_update", "workflow1_search_state",
           "workflow4_search", "workflow4_accept", "workflow4_reject"],
    "am": ["workflow1_accept", "workflow1_reject", "workflow1_search_state"],
    "sub_team": ["workflow2_plan", "workflow2_send", "workflow2_record_number", "workflow2_search_state",
                 "workflow2_comment"],
    "pm": ["workflow2_sub_team", "workflow2_task", "workflow2_send", "workflow2_record_number",
           "workflow2_search_state",
           "workflow3_contact_type", "workflow3_department", "workflow3_exp", "workflow3_title", "workflow3_jobdesc",
           "workflow3_send", "workflow3_form_ID", "workflow3_search",
           "workflow4_department", "workflow4_project_ref", "workflow4_amount", "workflow4_reason",
           "workflow4_search", "workflow4_send"],
    "hr": ["workflow3_search", "workflow3_applicant", "workflow3_send", "workflow3_form_ID"]
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

workflow3_contact_type = False
workflow3_form_ID = False
workflow3_department = False
workflow3_exp = False
workflow3_title = False
workflow3_jobdesc = False
workflow3_send = False
workflow3_search = False
workflow3_applicant = False

workflow4_search = False
workflow4_department = False
workflow4_project_ref = False
workflow4_amount = False
workflow4_reason = False
workflow4_send = False
workflow4_accept = False
workflow4_reject = False


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

    if "workflow3_search" not in Privileges[permission]:
        global workflow3_search
        workflow3_search = True
    if "workflow3_contact_type" not in Privileges[permission]:
        global workflow3_contact_type
        workflow3_contact_type = True
    if "workflow3_department" not in Privileges[permission]:
        global workflow3_department
        workflow3_department = True
    if "workflow3_exp" not in Privileges[permission]:
        global workflow3_exp
        workflow3_exp = True
    if "workflow3_title" not in Privileges[permission]:
        global workflow3_title
        workflow3_title = True
    if "workflow3_jobdesc" not in Privileges[permission]:
        global workflow3_jobdesc
        workflow3_jobdesc = True
    if "workflow3_send" not in Privileges[permission]:
        global workflow3_send
        workflow3_send = True
    if "workflow3_applicant" not in Privileges[permission]:
        global workflow3_applicant
        workflow3_applicant = True

    if "workflow4_search" not in Privileges[permission]:
        global workflow4_search
        workflow4_search = True
    if "workflow4_department" not in Privileges[permission]:
        global workflow4_department
        workflow4_department = True
    if "workflow4_project_ref" not in Privileges[permission]:
        global workflow4_project_ref
        workflow4_project_ref = True
    if "workflow4_amount" not in Privileges[permission]:
        global workflow4_amount
        workflow4_amount = True
    if "workflow4_reason" not in Privileges[permission]:
        global workflow4_reason
        workflow4_reason = True
    if "workflow4_send" not in Privileges[permission]:
        global workflow4_send
        workflow4_send = True
    if "workflow4_accept" not in Privileges[permission]:
        global workflow4_accept
        workflow4_accept = True
    if "workflow4_reject" not in Privileges[permission]:
        global workflow4_reject
        workflow4_reject = True
