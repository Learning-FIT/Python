from .employee import Employee

class Staff(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.role_name = '一般社員'
        self.base_salary = 300000
        self.score = 1.0

    def salary(self):
        return int(self.base_salary * self.score)