"""
***Operator Overloading in Python: An Introduction***
=>Operator Overloading is a feature in Python that allows developers to re-define the behavior of mathematical and
comparison operators for custom data types.
This means that you can use the standard mathematical operators (+, -, *, /, etc.) and
comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types
 like int, float, and str.

Why do we need operator overloading?
=>Operator overloading allows you to create more readable and intuitive code.
 For instance, consider a custom class that represents a point in 2D space.
 You could define a method called 'add' to add two points together, but using the + operator makes the code
  more concise and readable:

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y) # prints 4, 6
How to overload an operator in Python?
=>You can overload an operator in Python by defining special methods in your class.
 These methods are identified by their names, which start and end with double underscores (__).
  Here are some of the most commonly overloaded operators and their corresponding special methods:

+ : __add__
- : __sub__
* : __mul__
/ : __truediv__
< : __lt__
> : __gt__
== : __eq__
For example, if you want to overload the + operator to add two instances of a custom class, you would define the add method:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _add_(self, other):
        return Point(self.x + other.x, self.y + other.y)
It's important to note that operator overloading is not limited to the built-in operators, you can overload any user-defined operator as well.

Conclusion
Operator overloading is a powerful feature in Python that allows you to create more readable and intuitive code.
 By redefining the behavior of mathematical and comparison operators for custom data types, you can write code
 that is both concise and expressive. However, it's important to use operator overloading wisely, as overloading
 the wrong operator or using it inappropriately can lead to confusing or unexpected behavior.

"""
class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    # def __add__(self,x):
    #     return f"{self.i+x.i}i+{self.j+x.j}j+{self.k+x.k}k"
    #to make it vector use a vector retun type
    def __add__(self,x):
        return Vector(self.i + x.i,self.j + x.j,self.k + x.k)

v1=Vector(3,5,6)
print(v1)

v2=Vector(1,2,3)
print(v2)

print(v1+v2)#it cannot add without defining add method
print(type(v1+v2))#it is a string type..we need to convert it into vector type
