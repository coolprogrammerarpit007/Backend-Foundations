from collections import namedtuple

# color = (55,155,255)

Color = namedtuple('Color',['red','green','blue'])
color = Color(55,75,78)
# print(color)
# print(color.red)
# print(color.green)
# print(color.blue)



# OOPS -> Object Oriented Programming
from datetime import datetime,date

class Employee:
    num_employees = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@microprixs.in'
        self.pay = pay
        
        Employee.num_employees += 1
        
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        return self.pay
    
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
    
    def __str__(self):
        return '{} {}'.format(self.full_name(),self.email)
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.full_name())
    
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
        
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    
class Developer(Employee):
    def __init__(self, first, last, pay,programming_lang):
        super().__init__(first, last, pay)
        self.programming_lang = programming_lang
        
class Manager(Employee):
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
            
        else:
            self.employees = employees
            
    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
            
    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('--->',emp.full_name())
            
            
employee1 = Employee('Arpit','Mishra',20000)
emp_2 = Employee('Test', 'Employee', 60000)
print(employee1 + emp_2)
print(employee1.__repr__())
print(employee1.__str__())

# developer1 = Developer('Divyansh','Kumar',30000,'PHP/Laravel')
# # print(developer1.email)
# # developer1.apply_raise()
# # print(developer1.pay)
# # print(developer1.programming_lang)


# Employee.set_raise_amount(5)
# employee1 = Employee('Arpit','Mishra',20000)
# employee2 = Employee('Vikas','Sharma',15000)
# # print(employee1.apply_raise())



# today_date = date.today()
# # print(Employee.is_workday(today_date))

# mgr1 = Manager('Sue','Smith',50000,[developer1,employee1,employee2])
# mgr1.print_emps()
