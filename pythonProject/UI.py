import PySimpleGUI as sg
from login import permission
from helpers_for_workflow1 import search_request, add_request, update_request, check_send, send_request, accept_request, \
    reject_request
from helpers_for_workflow2 import search_event,send_event
from database import Privileges


permission = "cs"
workflow1_add_state = False
workflow1_send_state = False
workflow1_update_state = False
workflow1_accept_state = False
workflow1_reject_state = False
workflow1_search_state = False

workflow2_sub_team = False
workflow2_task = False
workflow2_plan = False
print(Privileges[permission])


def get_privilege():
    if "workflow1_add" not in Privileges[permission] == True:
        workflow1_add_state = True
    if "workflow1_view" not in Privileges[permission] == True:
        workflow1_send_state = True
    if "workflow1_update" not in Privileges[permission] == True:
        workflow1_update_state = True
    if "workflow1_accept" not in Privileges[permission] == True:
        workflow1_accept_state = True
    if "workflow1_reject" not in Privileges[permission] == True:
        workflow1_reject_state = True


get_privilege()
print(workflow1_add_state, workflow1_send_state, workflow1_update_state, workflow1_accept_state, workflow1_reject_state)


def make_window():
    layout_workflow1 = [
        [sg.Text('add'), sg.Input(s=15, key="add_record_name", disabled=workflow1_add_state),
         sg.Input(s=15, key="add_name", disabled=workflow1_add_state),
         sg.Input(s=15, key="add_description", disabled=workflow1_add_state),
         sg.Button("add", disabled=workflow1_add_state)],
        [sg.Multiline(key='view', size=(10, 10), font='courier 10', background_color='black', text_color='white',
                      expand_x=True, expand_y=True, disabled=workflow1_search_state),
         sg.Button(key="search_button", disabled=workflow1_search_state)],
        [sg.Text('update'), sg.Input(s=15, disabled=workflow1_update_state, key="workflow1_update"),
         sg.Input(s=15, disabled=workflow1_update_state, key="workflow1_update_record_name"),
         sg.Button(key="update_button", disabled=workflow1_update_state)],
        [sg.Text('send to next'), sg.Input(s=15, key="workflow1_send"), sg.Button(s=15, key="send_button")],
        [sg.Text('accept'), sg.Input(s=15, key="workflow1_accept"),
         sg.Button(s=15, disabled=workflow1_accept_state, key="accept_button")],
        [sg.Text('reject'), sg.Input(s=15, key="workflow1_reject"),
         sg.Button(s=15, disabled=workflow1_reject_state, key="reject_button")]]

    layout_workflow2 = [
        [sg.Multiline(key='workflow2_view', size=(10, 10), font='courier 10', background_color='black',
                      text_color='white',
                      expand_x=True, expand_y=True),
         sg.Button(key="workflow2_search_button")],
        [sg.Text('record_number'), sg.Input(s=15, key="workflow2_record_number")],
        [sg.Text('sub_team'), sg.Input(s=15, disabled=workflow2_sub_team, key="workflow2_sub_team")],
        [sg.Text('task'), sg.Input(s=15, disabled=workflow2_task, key="workflow2_task")],
        [sg.Text('plan'), sg.Input(s=15, disabled=workflow2_plan, key="workflow2_plan")],
        [sg.Text('comment'), sg.Input(s=15, disabled=workflow2_plan, key="workflow2_comment")],
        [sg.Text('send'), sg.Button(s=15, key="workflow2_send")]
    ]

    layout = [[sg.T('seb business', font='_ 14', justification='c', expand_x=True)],
              [sg.Col(layout_workflow1), sg.Col(layout_workflow2)]]

    window = sg.Window('The PySimpleGUI Element List', layout, finalize=True,
                       right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True)
    return window


window = make_window()

while True:
    event, values = window.read()
    # sg.Print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == "add":
        record_name = values["add_record_name"]
        name = values["add_name"]
        description = values["add_description"]
        add_request(record_name, name, description)
    if event == "search_button":
        window["view"].update("search result:\r\n", autoscroll=True, append=True)
        for i in search_request():
            window["view"].update(i, autoscroll=True, append=True)
            window["view"].update("\r\n", autoscroll=True, append=True)
    if event == "update_button":
        update_description = values["workflow1_update"]
        update_record_name = values["workflow1_update_record_name"]
        update_request(update_description, update_record_name)
    if event == "workflow1_send":
        send_record_name = values["workflow1_send"]
        if check_send(send_record_name):
            send_request(send_record_name)
        else:
            sg.popup("send fail")
    if event == "accept_button":
        accept_record_name = values["workflow1_accept"]
        accept_request(accept_record_name)
    if event == "reject_button":
        reject_record_name = values["workflow1_reject"]
        reject_request(reject_record_name)
    if event == "workflow2_search_button":
        window["workflow2_view"].update("search result:\r\n", autoscroll=True, append=True)
        for i in search_event():
            window["workflow2_view"].update(i.get_client_record_name() + " " + i.get_sub_team() + " " + i.get_plan()
                                            + " " + i.get_task() + " " + i.get_comment(),
                                            autoscroll=True, append=True)
            window["workflow2_view"].update("\r\n", autoscroll=True, append=True)
    if event == "workflow2_send":
        record_name= values["workflow2_record_number"]
        sub_team = values["workflow2_sub_team"]
        task = values["workflow2_task"]
        plan = values["workflow2_task"]
        comment = values["workflow2_comment"]
        send_event(permission,record_name,sub_team,task,plan,comment)


window.close()
