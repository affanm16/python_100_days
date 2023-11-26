"""
***self parameter****
=>The self parameter is a reference to the current instance of the class, and is used to access
    variables that belongs to the class.

=>It must be provided as the extra parameter inside the method definition.
"""
# Example:
class Details:
    name = "Rohan"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj2=Details()
obj2.name="affan"
obj2.age=20
obj1.desc()
obj2.desc()
