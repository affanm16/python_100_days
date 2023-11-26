"""
=>Static methods in Python are methods that belong to a class rather than an instance of the class.
=>They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self).
=>They are called on the class itself, not on an instance of the class.
=>Static methods are often used to create utility functions that don't need access to instance data.
"""
class Math:
    def __init__(self,num):#constructor
        self.num=num
    def addtonum(self,n):
        self.num=self.num+n


    def add(a,b):
        return a+b


    @staticmethod#you can call it directly,but it is inside the class without using self
    def add(a, b):
        return a + b
a=Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(a.add(10,20))

# result = Math.add(1, 2)
# print(result) # Output: 3
# =>In this example, the add method is a static method of the Math class.
# It takes two parameters a and b and returns their sum.
# The method can be called on the class itself, without the need to create an instance of the class.

