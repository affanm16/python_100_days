"""
***public Access Specifier in Python****
=>All the variables and methods (member functions) in python are by default public.
    Any instance variable in a class followed by the ‘self’ keyword i.e. self.var_name are public accessed.
"""
# Example:
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"affan")
print(obj.age)
print(obj.name)