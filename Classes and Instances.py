"""class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Attama'
emp_1.last = 'Pascalpedro'
emp_1.email = 'Attamapascalpedro@gmail.com'
emp_1.pay = 50000

emp_2.first = 'Lord'
emp_2.last = 'Pedro'
emp_2.email = 'Lordpedro@gmail.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))
print('{} {}'.format(emp_2.first, emp_2.last))"""




class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Attama', 'Pascal', 50000)
emp_2 = Employee('Lord', 'Pedro', 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
