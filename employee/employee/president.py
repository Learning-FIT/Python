from .employee import Employee

class President(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.role_name = '社長'
        self.base_salary = 500000