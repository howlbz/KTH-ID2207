import database

permission = "fm"


def login(username, password) -> bool:
    if username in database.Employees.keys():
        if database.Employees.values(username)[0] == password:
            permission = database.Employees.values()[1]
            return True
        else:
            return False
