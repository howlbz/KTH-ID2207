import PySimpleGUI as sg
from login import login


def make_login_window():
    layout = [[sg.Text('username'), sg.Input("Jack", s=15, key="username")],
              [sg.Text('password'), sg.Input("12345", s=15, key="password")],
              [sg.Button("enter"), sg.Button("exit")]
              ]

    main_window = sg.Window('Login SEP', layout, finalize=True,
                            right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True)
    return main_window


def display_login_window():
    window = make_login_window()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "exit":
            break
        if event == "enter":
            username = values["username"]
            password = values["password"]
            global permission
            permission = login(username, password)
            if permission != "none":
                window.close()
                return permission
            else:
                sg.popup("login Failed")

