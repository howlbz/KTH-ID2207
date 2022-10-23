import helpers_for_workflow1
import database


def test_add_request():
    helpers_for_workflow1.add_request("1000", "test", "test_description")

    assert database.Request_list["1000"][1].get_client_name() == "test"
    assert database.Request_list["1000"][1].get_description() == "test_description"


def test_update_request():
    helpers_for_workflow1.update_request("124", "test_update_description", "fm")
    assert database.Request_list["124"][1].get_description() == "test_update_description"


def test_workflow1():
    test_update_request()
    test_add_request()
    print("workflow1 passed!")


