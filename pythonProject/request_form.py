class Request_form:

    def __init__(self, client_record_name, client_name, description):
        self.description = description
        self.client_name = client_name
        self.client_record_name = client_record_name

    def get_client_record_name(self):
        return self.client_record_name

    def get_client_name(self):
        return self.client_name

    def get_description(self):
        return self.description

    def update_description(self,update_description):
        self.description = update_description

# class Request_form:
#
#     Client_record_name = None
#     Client_name = None
#     Event_type = None
#     Description = None
#     Expected_number = None
#     Planned_budget =None
#     From_data = None
#     To_data = None
#     Decorations = None
#     Food = None
#     Filming = None
#     Music = None
#     Posters =None
#     Computer_related_issues=None
#     Other = None
#
#     def __int__(self,client_record_name, client_name, event_type, description, expected_number, planned_budget,
#                 from_data, to_data, decorations, food, filming, music, posters, computer_related_issues, other):
#         self.Other = other
#         self.Computer_related_issues = computer_related_issues
#         self.Posters = posters
#         self.Music = music
#         self.Filming = filming
#         self.Food = food
#         self.Decorations = decorations
#         self.To_data = to_data
#         self.From_data = from_data
#         self.Planned_budget = planned_budget
#         self.Expected_number = expected_number
#         self.Description = description
#         self.Event_type = event_type
#         self.Client_name = client_name
#         self.Client_record_name = client_record_name
