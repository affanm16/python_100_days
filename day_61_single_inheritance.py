"""
***Single Inheritance****:
=>Single inheritance enables a derived class to inherit properties from a single parent class,
    thus enabling code reusability and the addition of new features to existing code.
"""
# Example:
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child(Parent):
    def func2(self):
        print("This function is in child class.")


object = Child()
object.func1()
object.func2()
