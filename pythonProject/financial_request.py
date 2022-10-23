class Financial_request:

    def __init__(self, department, project_ref, amount, reason):
        self.department = department
        self.project_ref = project_ref
        self.amount = amount
        self.reason = reason

    def get_department(self):
        return self.department

    def get_project_ref(self):
        return self.project_ref

    def get_amount(self):
        return self.amount

    def get_reason(self):
        return self.reason
