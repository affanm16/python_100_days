"""
****Python Tuples******
=>Tuples are ordered collection of data items.
=>They store multiple items in a single variable.
=>Tuple items are separated by commas and enclosed within round brackets ().
=>Tuples are unchangeable meaning we can not alter them after creation.
"""
#Example 1:
tuple1 = (10,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

#example 2
tup1=(10,100)
#tup1=(10,)
tup2=(10,20)
print(type(tup1))#it will show int instead of tuple,to avoid that put comma after the element
print(type(tup2))

#Example 3:
details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)