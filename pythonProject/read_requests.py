from request_form import Request_form
import database


def read_requests():
    f = open("read_requests.txt")
    lines = f.readlines()
    for line in lines:
        line.replace('\n', '')
        x = line.replace('\n', '').split(" ")
        request = Request_form(x[1], x[2], x[3])
        database.Request_list[x[1]] = [x[0], request, x[4]]

