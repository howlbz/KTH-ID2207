import helpers_for_workflow2
import database


def test_send_event():
    helpers_for_workflow2.send_event("pm", "2000", "test_team", "test_workflow2")
    for i in database.Event_list:
        if i.client_record_name == "2000":
            assert i.task == "test_workflow2"
            assert i.sub_team == "test_team"

    helpers_for_workflow2.send_event("sub_team", "2000", "test_team", "test_workflow2", "test_plan", "test_comment")
    for i in database.Event_list:
        if i.client_record_name == "2000":
            assert i.plan == "test_plan"
            assert i.comment == "test_comment"


def test_workflow2():
    test_send_event()
    print("workflow2 passed!")
