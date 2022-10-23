class Recruitment_result:

    def __init__(self, applicant, appjob, decision):
        self.applicant = applicant
        self.appjob = appjob
        self.decision = decision

    def get_applicant(self):
        return self.applicant

    def get_appjob(self):
        return self.appjob

    def get_decision(self):
        return self.decision
