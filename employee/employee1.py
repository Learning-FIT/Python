class Employee:
    def __init__(self, name):
        self.name = name
        self.role_name = ''

    def print(self):
        print(f'{self.name}さんは、{self.role_name}です。')

class President(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.role_name = '社長'    

class Staff(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.role_name = '一般社員'

def main():
    inoue = President('井上')
    print('クラス名', type(inoue))
    inoue.print()

if __name__ == '__main__':
    main()
