# Build an Employee class with:
# - Use @property for email (computed from first_name, last_name)
# - Use @property for full_name
# - Use @full_name.setter to allow setting full name and split into first/last
# - Use @full_name.deleter to set names to None

# Also create these standalone decorators:
# - @timer: prints how long a function takes to run
# - @logger: prints function name and arguments when called


class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property # managed attributes
    def email(self):
        return '{}.{}@gmail.com'.format(self.first_name, self.last_name)
    
    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name
    
    @full_name.deleter
    def full_name(self):
        print("name deleted")
        self.first_name = None
        self.last_name = None

