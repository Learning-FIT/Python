class Company:
    def __init__(self):
        self.employees = []

    def total_salary(self):
        total = 0
        for employee in self.employees:
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

def main():
    company = Company()

    inoue = President('井上')
    company.employees.append(inoue)

    suzuki = Staff('鈴木')
    suzuki.score = 1.2
    company.employees.append(suzuki)

    print(f'合計は、{company.total_salary():,}円です。')

if __name__ == '__main__':
    main()