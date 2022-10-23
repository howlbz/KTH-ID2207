import PySimpleGUI as sg
import privileges
from helpers_for_workflow1 import search_request, add_request, update_request, check_send, send_request, accept_request, \
    reject_request, test_search
from helpers_for_workflow2 import search_event, send_event
from helpers_for_workflow3 import search_rec_request, send_rec_request
from helpers_for_workflow4 import search_freq, send_freq, accept_freq, reject_freq


def make_main_window(permission):
    test_layout = [[sg.Multiline(key='test_view', size=(10, 10), font='courier 10', background_color='black',
                                 text_color='white', expand_x=True, expand_y=True),
                    sg.Button("view", key="test_search_button")]]
    layout_workflow1 = [
        [sg.Text('add'), sg.Input("100", s=15, key="add_record_name", disabled=privileges.workflow1_add_state),
         sg.Input("Alice", s=15, key="add_name", disabled=privileges.workflow1_add_state),
         sg.Input("Party", s=15, key="add_description", disabled=privileges.workflow1_add_state),
         sg.Button("add", disabled=privileges.workflow1_add_state)],
        [sg.Multiline(key='view', size=(10, 10), font='courier 10', background_color='black', text_color='white',
                      expand_x=True, expand_y=True),
         sg.Button("view", key="search_button", disabled=privileges.workflow1_search_state)],
        [sg.Text('update'), sg.Input("124", s=15, disabled=privileges.workflow1_update_state, key="workflow1_update"),
         sg.Input("good birthday", s=15, disabled=privileges.workflow1_update_state,
                  key="workflow1_update_record_name"),
         sg.Button("update", key="update_button", disabled=privileges.workflow1_update_state)],
        [sg.Text('send to next'), sg.Input("124", s=15, key="workflow1_send", disabled=privileges.workflow1_send_state),
         sg.Button("send", s=15, key="send_button", disabled=privileges.workflow1_send_state)],
        [sg.Text('accept'), sg.Input("200", s=15, key="workflow1_accept", disabled=privileges.workflow1_accept_state),
         sg.Button("accept", s=15, disabled=privileges.workflow1_accept_state, key="accept_button")],
        [sg.Text('reject'), sg.Input("200", s=15, key="workflow1_reject", disabled=privileges.workflow1_reject_state),
         sg.Button("reject", s=15, disabled=privileges.workflow1_reject_state, key="reject_button")]]

    layout_workflow2 = [
        [sg.Multiline(key='workflow2_view', size=(10, 10), font='courier 10', background_color='black',
                      text_color='white',
                      expand_x=True, expand_y=True),
         sg.Button("view", key="workflow2_search_button", disabled=privileges.workflow2_search)],
        [sg.Text('record_number'),
         sg.Input("300", s=15, disabled=privileges.workflow2_record_number, key="workflow2_record_number")],
        [sg.Text('sub_team'),
         sg.Input("Audio_specialist", s=15, disabled=privileges.workflow2_sub_team, key="workflow2_sub_team")],
        [sg.Text('task'), sg.Input("ceremony", s=15, disabled=privileges.workflow2_task, key="workflow2_task")],
        [sg.Text('plan'), sg.Input("a good plan", s=15, disabled=privileges.workflow2_plan, key="workflow2_plan")],
        [sg.Text('comment'),
         sg.Input("extra 100$", s=15, disabled=privileges.workflow2_comment, key="workflow2_comment")],
        [sg.Text('send'), sg.Button("send", s=15, disabled=privileges.workflow2_send, key="workflow2_send")]
    ]

    layout_workflow3 = [
        [sg.Multiline(key='workflow3_view', size=(10, 10), font='courier 10', background_color='black',
                      text_color='white',
                      expand_x=True, expand_y=True),
         sg.Button("view", key="workflow3_search_button", disabled=privileges.workflow3_search)],
        [sg.Text('Form_ID'), sg.Input("2", s=15, disabled=privileges.workflow3_form_ID,
                                      key="workflow3_form_ID")],
        [sg.Text('Contact_type'), sg.Input("Full time", s=15, disabled=privileges.workflow3_contact_type,
                                           key="workflow3_contact_type")],
        [sg.Text('Department'), sg.Input("Production", s=15,
                                         disabled=privileges.workflow3_department, key="workflow3_department")],
        [sg.Text('EXPYears'), sg.Input("1 year minimum", s=15, disabled=privileges.workflow3_exp,
                                       key="workflow3_exp")],
        [sg.Text('Job_title'), sg.Input("Chef", s=15, disabled=privileges.workflow3_title,
                                        key="workflow3_title")],
        [sg.Text('Job_Description'), sg.Input("Cooking", s=15, disabled=privileges.workflow3_jobdesc,
                                              key="workflow3_jobdesc")],
        [sg.Text('Send'), sg.Button("send", s=15, disabled=privileges.workflow3_send, key="workflow3_send")],
        [sg.Text('Approved_Applicant'), sg.Input("Applicant Name", s=15, disabled=privileges.workflow3_applicant,
                                                 key="workflow3_applicant")]
    ]

    layout_workflow4 = [
        [sg.Multiline(key='workflow4_view', size=(10, 10), font='courier 10', background_color='black',
                      text_color='white',
                      expand_x=True, expand_y=True),
         sg.Button("view", key="workflow4_search_button", disabled=privileges.workflow4_search)],
        [sg.Text('Department'), sg.Input("Admin/Services/Production/Financial", s=15,
                                         disabled=privileges.workflow4_department, key="workflow4_department")],
        [sg.Text('Project Reference'), sg.Input("e12488", s=15,
                                                key="workflow4_project_ref")],
        [sg.Text('Required Amount'), sg.Input("5000SEK", s=15,
                                              disabled=privileges.workflow4_amount, key="workflow4_amount")],
        [sg.Text('Reason'), sg.Input("Needed for decoration", s=15,
                                     disabled=privileges.workflow4_reason, key="workflow4_reason")],
        [sg.Text('Send'), sg.Button("send", s=15, disabled=privileges.workflow4_send, key="workflow4_send")],
        [sg.Text('Accept No.'), sg.Input("12488", s=15, key="workflow4_accept", disabled=privileges.workflow4_accept),
         sg.Button("Accept", s=15, disabled=privileges.workflow4_accept, key="accept_freq_button")],
        [sg.Text('Reject No.'), sg.Input("12488", s=15, key="workflow4_reject", disabled=privileges.workflow4_reject),
         sg.Button("Reject", s=15, disabled=privileges.workflow4_reject, key="reject_freq_button")]

    ]

    # layout = [test_layout,
    #           [
    #               [sg.T('Swedish Events Planners SEP', font='_ 14', justification='c', expand_x=True)],
    #               [sg.Col(layout_workflow1), sg.Col(layout_workflow2)],
    #               [sg.Col(layout_workflow3), sg.Col(layout_workflow4)]
    #           ]]
    layout = [[sg.T('Swedish Events Planners SEP', font='_ 14', justification='c', expand_x=True)],
              [sg.TabGroup([[sg.Tab('test', test_layout),
                              sg.Tab('workflow1', layout_workflow1),
                              sg.Tab('workflow2', layout_workflow2),
                              sg.Tab('workflow3', layout_workflow3),
                              sg.Tab('workflow4', layout_workflow4)]], key='-TAB GROUP-', expand_x=True, expand_y=True),

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
            update_request(update_description, update_record_name, permission)

        if event == "send_button":
            send_record_name = values["workflow1_send"]
            if check_send(send_record_name):
                send_request(send_record_name)
            else:
                sg.popup("send fail")

        if event == "accept_button":
            accept_record_name = values["workflow1_accept"]
            accept_request(accept_record_name, permission)

        if event == "reject_button":
            reject_record_name = values["workflow1_reject"]
            reject_request(reject_record_name, permission)

        if event == "accept_freq_button":
            accept_project_ref = values["workflow4_accept"]
            accept_freq(accept_project_ref)

        if event == "reject_freq_button":
            reject_project_ref = values["workflow4_reject"]
            reject_freq(reject_project_ref)

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

        if event == "workflow3_search_button":
            window["workflow3_view"].update("search result:\r\n", autoscroll=True, append=True)
            for i in search_rec_request():
                window["workflow3_view"].update(i.get_form_ID() + "\n" + i.get_contact_type() + "\n " +
                                                i.get_department()+ "\n" + i.get_exp() + "\n" + i.get_title()
                                                + "\n" + i.get_jobdesc() + "\n" + i.get_applicant(),
                                                autoscroll=True, append=True)
                window["workflow3_view"].update("\r\n", autoscroll=True, append=True)

        if event == "workflow3_send":
            form_ID = values["workflow3_form_ID"]
            contact_type = values["workflow3_contact_type"]
            department = values["workflow3_department"]
            exp = values["workflow3_exp"]
            title = values["workflow3_title"]
            jobdesc = values["workflow3_jobdesc"]
            applicant = values["workflow3_applicant"]
            send_rec_request(permission, form_ID, contact_type, department, exp, title, jobdesc, applicant)

        if event == "workflow4_send":
            department = values["workflow4_department"]
            project_ref = values["workflow4_project_ref"]
            amount = values["workflow4_amount"]
            reason = values["workflow4_reason"]
            send_freq(department, project_ref, amount, reason)

        if event == "workflow4_search_button":
            window["workflow4_view"].update("search result:\r\n", autoscroll=True, append=True)
            for i in search_freq():
                for j in i :
                    window["workflow4_view"].update(j, autoscroll=True, append=True)
                    window["workflow4_view"].update("\r\n", autoscroll=True, append=True)

    window.close()


