class Employee:
    def __init__(self, name):
        self.name = name
        self.role_name = ''

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

def main():
    inoue = President('井上')
    inoue.print()
    suzuki = Staff('鈴木')
    suzuki.print()

if __name__ == '__main__':
    main()