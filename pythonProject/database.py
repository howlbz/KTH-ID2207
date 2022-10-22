from request_form import Request_form
from event_form import Event_form

Employees = {  # password position
    "Sam": ["Sam", "12345", "cs"],
    "Janet": ["Janet", "12345", "scs"],
    "John Doe": ["John Doe", "12345", "fm"],
    "Mike": ["Mike", "12345", "am"],
    "Jack": ["Jack", "12345", "pm"],
    "Julia": ["Julia", "12345", "sub_team"]
}

Request_list = {"124": ["fm", Request_form("124", "axe", "birthday"), "pending"],
                "200": ["am", Request_form("200", "sniper", "holiday party"), "pending"]}

prodcution_sub_team = ["Photographer", "Audio_specialist", "Graphic_designer", "Decorating_designer",
                       "Network_engineer"]

Event_list = [Event_form("124", "Photographer", "party", "TRADITIONAL MUSIC", "NO MORE REQUEST"),
              Event_form("200", "Network_engineer", "birthday", "", "")]
