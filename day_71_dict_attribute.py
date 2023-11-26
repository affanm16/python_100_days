# The _dict_ attribute
# __dict: The __dict__ attribute returns a dictionary representation of an object's attributes.
# It is a useful tool for introspection. Example:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person("John", 30)
print(p.__dict__)
