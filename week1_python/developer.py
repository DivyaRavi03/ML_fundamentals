# Build a Developer class that inherits from Employee:
# - Additional attribute: programming_language
# - Override apply_raise() to give developers 10% instead of company default
# - Add __str__ and __repr__ methods


class Employee:
    company_name = 'ABC'
    raise_percentage = 1.04
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)

    def email(self):
        return self.first_name + '.' + self.last_name + '@company.com'
        
    
    def full_name(self):
        return self.first_name + ' ' + self.last_name
        

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_percentage)
        return self.salary

class Developer(Employee):
    raise_percentage = 1.10
    def __init__(self, first_name, last_name, salary, programming_language):
        super().__init__(first_name, last_name, salary) 
        self.programming_language = programming_language

    def __repr__(self):
        return "Employee({} - {})".format(self.full_name(), self.email())
    
    def __str__(self):
        return '{} - {}'.format(self.full_name(), self.email())
    
dev_1 = Developer('John' , 'Jim', 5000, 'java')

print(dev_1)



# first program 
# class Employee:
#     raise_amount = 1.04
    
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@gmail.com'
        
#     def full_name(self):
#         return self.first + ' ' + self.last
        
#     def set_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#         return self.pay
        
# class Developer(Employee):
    
#     raise_amount = 1.10
    
#     def __init__(self,first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang

# class Manager(Employee):
#     def __init__(self, first, last, pay, employee = None):
#         super().__init__(first, last, pay)
#         if employee is None: 
#             self.employee = []
#         else:
#             self.employee = employee
        
#     def add_emp(self, emp):
#         if emp not in self.employee:
#             self.employee.append(emp)
    
#     def remove_emp(emp):
#         if emp in self.employee:
#             self.employee.remove(emp)
            
            
#     def print_emp(self):
#         for emp in self.employee:
#             print('-->', emp.full_name())
            

# dev_1 = Developer('Cor', 'S', 5000, 'java')
# dev_2 = Developer('Sasa', 'hjkf', 6000, 'C')
# mng_1 = Manager('kjhb', 'hgdv', 7000, [dev_1, dev_2])

# # dev_1.set_raise()
# # print(dev_1.pay)

# mng_1.set_raise()
# print(mng_1.pay)

# mng_1.print_emp()
        