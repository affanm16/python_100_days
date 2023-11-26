# Tuple methods
# As tuple is immutable type of collection of elements it have limited built in methods.

# count() Method
# The count() method of Tuple returns the number of times the given element appears in the tuple.

# Syntax:
# tuple.count(element)


#Example
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
t = tuple1.count(3)
print('Count of 3 in Tuple1 is:', t)


# index() method
# The Index() method returns the FIRST occurrence of the given element from the tuple.
# Syntax:
# tuple.index(element, start, end)
# Note: This method raises a ValueError if the element is not found in the tuple.

#Example
tuple = (0, 1, 2, 10, 20, 3, 2, 3, 1, 3, 2)
res = tuple.index(3)
var2=tuple.index(3,6,9)#slicing from index 6 to 8 and finding index of first 3
# var=tuple.index(15)
print('First occurrence of 3 is', res)
# print('First occurrence of 15 is', var)
print('First occurrence of 3 between index 6 to 9 is', var2)
#length()
print(len(tuple))