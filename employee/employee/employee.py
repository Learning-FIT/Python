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