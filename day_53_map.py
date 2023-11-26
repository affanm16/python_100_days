"""
***Map, Filter and Reduce****
=>In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to
    a sequence of elements and return a new sequence.
    These functions are known as higher-order functions, as they take other functions as arguments.

***map****
=>The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
 The map function has the following syntax:

map(function, iterable)
=>The function argument is a function that is applied to each element in the iterable argument.
 The iterable argument can be a list, tuple, or any other iterable object.


# List of numbers
numbers = [1, 2, 3, 4, 5]

# Double each number using the map function
doubled = map(lambda x: x * 2, numbers)

# Print the doubled numbers
print(list(doubled))
In the above example, the lambda function lambda x: x * 2 is used to double each element in the numbers list.
The map function applies the lambda function to each element in the list and returns a new list containing the doubled numbers.
"""
# example2
def cube(x):
    return x*x*x
print(cube(2))
l=[1,2,4,6,4,3]
# l1=[]#empty list
# for item in l:
#     l1.append(cube(item))
# print(l1)
#this can be done using map
new_list=list(map(cube,l))#without 'list' it gives map object which should be converted in list
print(new_list)

#example2
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Double each number using the map function
doubled = map(lambda x: x * 2, numbers)

# Print the doubled numbers
print(list(doubled))