class Recruitment_form:

    def __init__(self, form_ID, contact_type, department, exp, title, jobdesc, applicant):
        self.form_ID = form_ID
        self.contact_type = contact_type
        self.department = department
        self.exp = exp
        self.title = title
        self.jobdesc = jobdesc
        self.applicant = applicant

    def get_form_ID(self):
        return self.form_ID

    def get_contact_type(self):
        return self.contact_type

    def get_department(self):
        return self.department

    def get_exp(self):
        return self.exp

    def get_title(self):
        return self.title

    def get_jobdesc(self):
        return self.jobdesc

    def get_applicant(self):
        return self.applicant
