"""class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

emp_1 = Employee('Attama', 'Pascalpedro', 50000)
emp_2 = Employee('Lord', 'Pedro', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)"""




class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee('Attama', 'Pascalpedro', 50000)
emp_2 = Employee('Lord', 'Pedro', 60000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
