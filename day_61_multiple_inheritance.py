"""***Multilevel Inheritance*** :
=>In multilevel inheritance, features of the base class and the derived class are
  further inherited into the new derived class.
  This is similar to a relationship representing a child and a grandfather.

# Example:
"""


class Grandfather:

    def _init_(self, grandfathername):
        self.grandfathername = grandfathername


class Father(Grandfather):
    def _init_(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather._init_(self, grandfathername)


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father._init_(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


s1 = Son('Prince', 'pappa', 'munna')
print(s1.grandfathername)
s1.print_name()
