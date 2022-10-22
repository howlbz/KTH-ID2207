import database
from event_form import Event_form
from login import permission
from workflow import workflow2

def search_event():
    res = []
    for i in database.Event_list:
        res.append(i)
    return res

def send_event(permission="",record_name="",sub_team="",task="", plan="", comment=""):
    if permission == "pm":
        event = Event_form(record_name,sub_team,task, plan, comment)
        database.Event_list.append(event)
    elif permission == "sub_team":
        for i in database.Event_list:
            if i.client_record_name == record_name:
                i.plan=plan
                i.comment=comment







