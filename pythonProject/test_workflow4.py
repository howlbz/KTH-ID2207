import helpers_for_workflow4
import database


def test_send_freq():
    helpers_for_workflow4.send_freq("Production", "24888", "10000SEK", "Lack")

    assert database.Financial_req_list["24888"][1].get_department() == "Production"
    assert database.Financial_req_list["24888"][1].get_project_ref() == "24888"
    assert database.Financial_req_list["24888"][1].get_amount() == "10000SEK"
    assert database.Financial_req_list["24888"][1].get_reason() == "Lack"


def test_accept_freq():
    helpers_for_workflow4.accept_freq("12488")
    assert database.Financial_req_list["12488"][2] == "accepted"


def test_reject_freq():
    helpers_for_workflow4.reject_freq("12488")
    assert database.Financial_req_list["12488"][2] == "rejected"


def test_workflow4():
    test_send_freq()
    test_accept_freq()
    test_reject_freq()
    print("workflow4 passed!")
