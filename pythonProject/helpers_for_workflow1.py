import database
from request_form import Request_form
from login import permission
from workflow import workflow1

def search_request():
    res = []
    for key in database.Request_list.keys():
        if database.Request_list[key][0] == permission and database.Request_list[key][2] == "pending":
            res.append((database.Request_list[key][1].get_client_record_name(),
                       database.Request_list[key][1].get_client_name(),
                       database.Request_list[key][1].get_description(),
                       database.Request_list[key][2]))
    return res

def add_request(record_name, name, description):
    new_request = Request_form(record_name, name, description)
    database.Request_list[record_name] = ["fm", new_request, "pending"]

def update_request(update_description,update_record_name):
    database.Request_list[update_record_name][1].update_description(update_description)

def check_send(update_record_name):
    if database.Request_list[update_record_name][0] == "scs" and database.Request_list[update_record_name][2] != "pending":
        return False
    else:
        return True

def send_request(update_record_name):
    p = workflow1.index[database.Request_list[update_record_name][0]]
    database.Request_list[update_record_name][0] = workflow1[p+1]

def accept_request(accept_record_name):
    database.Request_list[accept_record_name][2] = "accepted"
    database.Request_list[accept_record_name][0] = "scs"

def reject_request(reject_record_name):
    database.Request_list[reject_record_name][2] = "rejected"
    database.Request_list[reject_record_name][0] = "scs"


