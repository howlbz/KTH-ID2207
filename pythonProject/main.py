from login_ui import display_login_window
from UI import display_main_window
from login import permission
from privileges import get_privilege
if __name__ == '__main__':
    permission = display_login_window()
    if permission != "none":
        get_privilege(permission)
        print(permission)
        display_main_window(permission)
