"""
****dir(), _dict_ and help() methods in python***
=>We must look into dir(), _dict_() and help() attribute/methods in python.
 They make it easy for us to understand how classes resolve various functions and executes code.
  In Python, there are three built-in functions that are commonly used to get information about objects:
   dir(), dict, and help(). Let's take a look at each of them:

***The dir() method****
=>dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for
an object.
It is a useful tool for discovering what you can do with an object. Example:
"""
x = [1, 2, 3]
print(dir(x))
print(x.__add__)


# >>> class Person:
# ...     def _init_(self, name, age):
# ...         self.name = name
# ...         self.age = age
# ...
# >>> p = Person("John", 30)
# >>> p._dict_
#
