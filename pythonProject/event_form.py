class Event_form:

    def __init__(self, client_record_name, sub_team, task, plan, comment):
        self.client_record_name = client_record_name
        self.sub_team = sub_team
        self.task = task
        self.plan = plan
        self.comment = comment

    def get_client_record_name(self):
        return self.client_record_name

    def get_sub_team(self):
        return self.sub_team

    def get_task(self):
        return self.task

    def get_plan(self):
        return self.plan

    def get_comment(self):
        return self.comment
