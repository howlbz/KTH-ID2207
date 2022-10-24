import helpers_for_workflow3
import database


def test_send_rec_request():
    helpers_for_workflow3.send_rec_request("pm", "10", "Full-time_test", "Admin_test", "NA_test", "title_test",
                                           "description_test")
    for i in database.Recruitment_list:
        if i.form_ID == "10":
            assert i.contact_type == "Full-time_test"
            assert i.department == "Admin_test"
            assert i.exp == "NA_test"
            assert i.title == "title_test"
            assert i.jobdesc == "description_test"

    helpers_for_workflow3.send_rec_request("hr", "12", "Full-time_test", "Admin_test", "NA_test", "title_test",
                                           "description_test", "Catty")
    for i in database.Recruitment_list:
        if i.form_ID == "12":
            assert i.applicant == "Catty"


def test_workflow3():
    test_send_rec_request()
    print("workflow3 passed!")
