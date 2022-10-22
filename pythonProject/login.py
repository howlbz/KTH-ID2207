import database

permission = "none"


def login(username="", password=""):
    if username in database.Employees.keys():
        if database.Employees[username][1] == password:
            global permission
            permission = database.Employees[username][2]
            return permission
        else:
            return permission
