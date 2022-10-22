from Employee import Employee
import database


def read_employees():
    f = open("employees.txt")
    lines = f.readlines()
    for line in lines:
        line.replace('\n', '')
        x = line.replace('\n', '').split(" ")
        employee = Employee(x[0] + " " + x[1], x[2], x[3])
        database.Employees[x[0] + " " + x[1]] = employee

