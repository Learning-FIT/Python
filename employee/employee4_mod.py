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

class Employee:
    def __init__(self, name):
        self.name = name
        self.role_name = ''
        self.base_salary = 0

    def print(self):
        print(f'{self.name}さんは、{self.role_name}です。')
        print(f'給料は{self.salary():,}円です。')

    def salary(self):
        return self.base_salary

class President(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.role_name = '社長'
        self.base_salary = 500000

class Staff(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.role_name = '一般社員'
        self.base_salary = 300000
        self.score = 1.0

    def salary(self):
        return int(self.base_salary * self.score)
