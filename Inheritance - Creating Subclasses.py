
""""# CREATING SUBCLASSES!!!
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10


dev_1 = Developer('Attama', 'Pascalpedro', 50000)
dev_2 = Developer('Lord', 'Pedro', 60000,)

# print(dev_1.pay)
# print(dev_2.pay)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)"""




"""# CREATING ADDITION FUNCTIONALITIES WITHIN A SUBCLASS!!!
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first,  last, pay)
        self.prog_lang = prog_lang


dev_1 = Developer('Attama', 'Pascalpedro', 50000, 'Python')
dev_2 = Developer('Lord', 'Pedro', 60000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)"""




# CREATING ANOTHER SUBCLASS!!!
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first,  last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Attama', 'Pascalpedro', 50000, 'Python')
dev_2 = Developer('Lord', 'Pedro', 60000, 'Java')

mgr_1 = Manager('Chukwu', 'Emeka', 90000, [dev_1])

# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.print_emp()

# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Manager))
print(issubclass(Manager, Manager))
print(issubclass(Employee, Manager))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Employee, Employee))
print(issubclass(Developer, Developer))
print(issubclass(Manager, Developer))
print(issubclass(Employee, Developer))