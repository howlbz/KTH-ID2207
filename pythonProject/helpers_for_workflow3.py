import database
from recruitment_form import Recruitment_form


def send_rec_request(permission="", form_ID="", contact_type="", department="", exp="", title="", jobdesc="",
                     applicant=""):
    if permission == "pm":
        recruitment = Recruitment_form(form_ID, contact_type, department, exp, title, jobdesc, "")

        database.Recruitment_list.append(recruitment)
    elif permission == "hr":
        for i in database.Recruitment_list:
            if i.form_ID == form_ID:
                i.applicant = applicant


def search_rec_request():
    res = []
    for i in database.Recruitment_list:
        res.append(i)
    return res
