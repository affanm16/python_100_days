"""
=>Check whether an item in present in the list?
We can check if a given item is present in the list.
 This is done using the 'in' keyword.


=>Range of Index:
You can print a range of list items by specifying where you want to start,
where do you want to end and if you want to skip elements in between the range.

Syntax:

listName[start : end : jumpIndex]

Note: jump Index is optional. We will see this in later examples.
Note: The element of the end index provided will not be included.

"""
#searching in list
marks=[50,55,"blue","raju",9.5]
if 55 in marks:
    print("yes")
else:
    print("NO")
#printing the list
print(marks)
print(marks[:])
#printing upto a range
print(marks[1:])
print(marks[1:-1])#len(marks)-1=5-1=4(postive index for -1)

#jump index
print(marks[0:len(marks):1])
print(marks[0:len(marks):2])