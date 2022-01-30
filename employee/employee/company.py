from .staff import Staff

class Company:
    def __init__(self):
        self.__employees = []

    def add_employee(self, employee):
        self.__employees.append(employee)

    def add_staff(self, name, score):
        staff = Staff(name)
        staff.score = score
        self.__employees.append(staff)

    def total_salary(self):
        total = 0
        for employee in self.__employees:
            total += employee.salary()
        return total