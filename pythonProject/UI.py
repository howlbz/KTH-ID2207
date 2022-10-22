import PySimpleGUI as sg
import privileges
from helpers_for_workflow1 import search_request, add_request, update_request, check_send, send_request, accept_request, \
    reject_request, test_search
from helpers_for_workflow2 import search_event, send_event


def make_main_window(permission):
    test_layout = [[sg.Multiline(key='test_view', size=(10, 10), font='courier 10', background_color='black',
                                 text_color='white', expand_x=True, expand_y=True),
                    sg.Button("view", key="test_search_button")]]
    layout_workflow1 = [
        [sg.Text('add'), sg.Input("100",s=15, key="add_record_name", disabled=privileges.workflow1_add_state),
         sg.Input("Alice",s=15, key="add_name", disabled=privileges.workflow1_add_state),
         sg.Input("Party",s=15, key="add_description", disabled=privileges.workflow1_add_state),
         sg.Button("add", disabled=privileges.workflow1_add_state)],
        [sg.Multiline(key='view', size=(10, 10), font='courier 10', background_color='black', text_color='white',
                      expand_x=True, expand_y=True),
         sg.Button("view", key="search_button", disabled=privileges.workflow1_search_state)],
        [sg.Text('update'), sg.Input("124",s=15, disabled=privileges.workflow1_update_state, key="workflow1_update"),
         sg.Input("good birthday", s=15, disabled=privileges.workflow1_update_state, key="workflow1_update_record_name"),
         sg.Button("update", key="update_button", disabled=privileges.workflow1_update_state)],
        [sg.Text('send to next'), sg.Input("124", s=15, key="workflow1_send",disabled=privileges.workflow1_send_state),
         sg.Button("send", s=15, key="send_button", disabled=privileges.workflow1_send_state)],
        [sg.Text('accept'), sg.Input("200",s=15, key="workflow1_accept", disabled=privileges.workflow1_accept_state),
         sg.Button("accept", s=15, disabled=privileges.workflow1_accept_state, key="accept_button")],
        [sg.Text('reject'), sg.Input("200",s=15, key="workflow1_reject", disabled=privileges.workflow1_reject_state),
         sg.Button("reject", s=15, disabled=privileges.workflow1_reject_state, key="reject_button")]]

    layout_workflow2 = [
        [sg.Multiline(key='workflow2_view', size=(10, 10), font='courier 10', background_color='black',
                      text_color='white',
                      expand_x=True, expand_y=True),
         sg.Button("view", key="workflow2_search_button", disabled=privileges.workflow2_search)],
        [sg.Text('record_number'),
         sg.Input("300",s=15, disabled=privileges.workflow2_record_number, key="workflow2_record_number")],
        [sg.Text('sub_team'), sg.Input("Audio_specialist",s=15, disabled=privileges.workflow2_sub_team, key="workflow2_sub_team")],
        [sg.Text('task'), sg.Input("ceremony", s=15, disabled=privileges.workflow2_task, key="workflow2_task")],
        [sg.Text('plan'), sg.Input("a good plan", s=15, disabled=privileges.workflow2_plan, key="workflow2_plan")],
        [sg.Text('comment'), sg.Input("extra 100$",s=15, disabled=privileges.workflow2_comment, key="workflow2_comment")],
        [sg.Text('send'), sg.Button("send",s=15, disabled=privileges.workflow2_send, key="workflow2_send")]
    ]

    layout = [test_layout,
              [
                  [sg.T('Swedish Events Planners SEP', font='_ 14', justification='c', expand_x=True)],
                  [sg.Col(layout_workflow1), sg.Col(layout_workflow2)]
              ]]

    main_window = sg.Window('Swedish Events Planners SEP', layout)
    return main_window


def display_main_window(permission):
    window = make_main_window(permission)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == "test_search_button":
            window["test_view"].update("search result:\r\n", autoscroll=True, append=True)
            for i in test_search():
                window["test_view"].update(i, autoscroll=True, append=True)
                window["test_view"].update("\r\n", autoscroll=True, append=True)
        if event == "add":
            record_name = values["add_record_name"]
            name = values["add_name"]
            description = values["add_description"]
            add_request(record_name, name, description)

        if event == "search_button":
            window["view"].update("search result:\r\n", autoscroll=True, append=True)
            for i in search_request(permission):
                window["view"].update(i, autoscroll=True, append=True)
                window["view"].update("\r\n", autoscroll=True, append=True)

        if event == "update_button":
            update_description = values["workflow1_update"]
            update_record_name = values["workflow1_update_record_name"]
            update_request(update_description, update_record_name,permission)

        if event == "send_button":
            send_record_name = values["workflow1_send"]
            if check_send(send_record_name):
                send_request(send_record_name)
            else:
                sg.popup("send fail")

        if event == "accept_button":
            accept_record_name = values["workflow1_accept"]
            accept_request(accept_record_name,permission)

        if event == "reject_button":
            reject_record_name = values["workflow1_reject"]
            reject_request(reject_record_name,permission)

        if event == "workflow2_search_button":
            window["workflow2_view"].update("search result:\r\n", autoscroll=True, append=True)
            for i in search_event():
                window["workflow2_view"].update(i.get_client_record_name() + " " + i.get_sub_team() + " " + i.get_task()
                                                + " " + i.get_plan() + " " + i.get_comment(),
                                                autoscroll=True, append=True)
                window["workflow2_view"].update("\r\n", autoscroll=True, append=True)

        if event == "workflow2_send":
            record_name = values["workflow2_record_number"]
            sub_team = values["workflow2_sub_team"]
            task = values["workflow2_task"]
            plan = values["workflow2_plan"]
            comment = values["workflow2_comment"]
            send_event(permission, record_name, sub_team, task, plan, comment)
    window.close()
