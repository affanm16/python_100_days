"""
***List Comprehension***
List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries,
sets, and even in arrays and strings.

Syntax:
List = [Expression(item) for item in iterable if Condition]

Expression: It is the item which is being iterated.

Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

Condition: Condition checks if the item should be added to the new list or not.


Example 1: Accepts items with the small letter “o” in the new list


Example 2: Accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
Output:
['Sarah', 'Bruno', 'Anastasia']
"""
#example 1
list =[i for i in range(10)]#range 10=total 10 items
print(list)

#example 2->creating list from a list
teachers=["a","b","c","d","e","f"]
present=[i for i in range(5)]
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
print(present)

#example3->using conditions
list1 = [item for item in names if "o" in item]
print(list1)
