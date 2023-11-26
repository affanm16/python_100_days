"""
***Python Class and Objects****
=>A class is a blueprint or a template for creating objects, providing initial values for state (member variables
    or attributes), and implementations of behavior (member functions or methods).
    The user-defined objects are created using the class keyword.

=>Creating a Class:
=>Let us now create a class using the class keyword.

class Details:
    name = "Rohan"
    age = 20
***Creating an Object****:
=>Object is the instance of the class used to access the properties of the class Now let's create an object of the class.

Example:
obj1 = Details()
Now we can print values:

Example:
class Details:
    name = "Rohan"
    age = 20

obj1 = Details()
print(obj1.name)
print(obj1.age)
"""
# example1
class person:
    name="harry"
    occupation="coder"
    networth=20000
print(person.name,person.occupation,person.networth)
a=person()#creating object of person 'a'
a.name="arun"
a.occupation="teacher"
a.networth=1000
print(a.name,a.occupation,a.networth)
#example2
class word:
    name="affan"
    occupation="student"
    def info(self):
        print(f"{self.name} is a {self.occupation}")
c=word()
c.info()