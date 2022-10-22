from request_form import Request_form
from Employee import Employee
from event_form import  Event_form

Employees = {  # password position
    "John Doe": ["John Doe", "12345", "fm"]
}

Request_list = {124: ["fm", Request_form("124", "axe", "birthday"), "pending"]}

Privileges = {
    "cs": ["workflow1_add", "workflow1_send"],
    "scs": ["workflow1_send", "workflow1_update", "workflow1_reject"],
    "fm": ["workflow1_send", "workflow1_update"],
    "am": ["workflow1_accept", "workflow1_reject"],
    "sub_team":[],
    "pm":[]
}

prodcution_sub_team =["Photographer", "Audio_specialist", "Graphic_designer", "Decorating_designer", "Network_engineer"]

Event_list = [Event_form("124", "Photographer","MUSIC", "TRADITIONAL MUSIC","NO MORE REQUEST")]

def employees():
    return None
