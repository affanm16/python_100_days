"""
***Python Lists****
->Lists are ordered collection of data items.
->They store multiple items in a single variable.
->List items are separated by commas and enclosed within square brackets [].
->Lists are changeable meaning we can alter them after creation.

=>Example 1:

lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)
Output:

[1, 2, 2, 3, 5, 4, 6]
['Red', 'Green', 'Blue']
=>Example 2:

details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)
Output:

['Abhijeet', 18, 'FYBScIT', 9.8]
->As we can see, a single list can contain items of different data types.

22 Day 22 -Introduction to Lists
22 Day 22 -Introduction to Lists


**List Index**

Each item/element in a list has its own unique index. This index can be used to access any particular item from the list.
The first item has index [0], second item has index [1], third item has index [2] and so on.

Example:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]

**Accessing list items**
We can access list items by using its index with the square bracket syntax [].
For example colors[0] will give "Red", colors[1] will give "Green" and so on...

Positive Indexing:
As we have seen that list items have index, as such we can access items using these indexes.

Example:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])
Output:
Blue
Green
Red

**Negative Indexing**:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the list.
The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

Example:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])
Output:
Green
Blue
Red

"""
marks=[3,5,20]
list1=[1,2,"python",True]#true is a boolean,python is string
print(marks)
print(type(marks))#index starts from 0
print(marks[0])
print(marks[1])
print(marks[2])
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])

#negative indexing
print(marks[-1])
print(list1[-3])

