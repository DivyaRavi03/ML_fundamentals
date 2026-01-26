# Build an Employee class with:
# - Class variable: company_name, raise_percentage (shared across all employees)
# - Instance variables: first_name, last_name, salary
# - Property: email (returns firstname.lastname@company.com)
# - Property: full_name
# - Method: apply_raise() - increases salary by raise_percentage
# - Class method: set_raise_percentage() - changes raise for all employees
# - Class method: from_string() - creates Employee from "John-Doe-50000" format


class Employee:
    company_name = 'ABC'
    raise_percentage = 1.04
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)
    
    def email(self):
        self.email = self.first_name + '.' + self.last_name + '@company.com'
        return self.email
    
    def full_name(self):
        self.full_name = self.first_name + ' ' + self.last_name
        return self.full_name

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_percentage)

    @classmethod
    def set_raise_percentage(cls, amount):
        cls.raise_percentage = amount

    @classmethod
    def from_string(cls, emp_strng):
        first, last, salary = emp_strng.split('-')
        return cls(first, last, salary)


emp_1 = 'John-Doe-50000'
new_emp_1 = Employee.from_string(emp_1)
print(new_emp_1.full_name())
print(new_emp_1.email())
print(new_emp_1.salary)
new_emp_1.apply_raise() # call first
print(new_emp_1.salary) # print salary later
Employee.set_raise_percentage(1.07) # call classmethod
new_emp_1.apply_raise()
print(new_emp_1.salary)

