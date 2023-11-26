"""
***Manipulating Tuples***
=>Tuples are immutable, hence if you want to add, remove or change tuple items,
=>then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

Output:
('Spain', 'Italy', 'Finland', 'Germany', 'Russia')
Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.



"""
#Example1:
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
#However, we can directly concatenate two tuples without converting them to list.
#Example:
countries1 = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = (countries1 + countries2)
print(southEastAsia)