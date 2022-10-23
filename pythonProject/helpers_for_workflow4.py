import database
from financial_request import Financial_request


def search_freq():
    res = []
    for key in database.Financial_req_list.keys():
        print(key)
        print()
        print((database.Financial_req_list[key][1].get_department(),
               database.Financial_req_list[key][1].get_project_ref(),
               database.Financial_req_list[key][1].get_amount(),
               database.Financial_req_list[key][1].get_reason(),
               database.Financial_req_list[key][2]))
        res.append((database.Financial_req_list[key][1].get_department(),
                    database.Financial_req_list[key][1].get_project_ref(),
                    database.Financial_req_list[key][1].get_amount(),
                    database.Financial_req_list[key][1].get_reason(),
                    database.Financial_req_list[key][2]))
    return res


def send_freq(department, project_ref, amount, reason):
    new_request = Financial_request(department, project_ref, amount, reason)
    database.Financial_req_list[project_ref] = ["pm", new_request, "pending"]


def accept_freq(accept_project_ref):
    if accept_project_ref in database.Financial_req_list.keys():
        database.Financial_req_list[accept_project_ref][2] = "accepted"


def reject_freq(reject_project_ref):
    if reject_project_ref in database.Financial_req_list.keys():
        database.Financial_req_list[reject_project_ref][2] = "rejected"
