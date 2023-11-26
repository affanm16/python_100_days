"""
***filter***
=>The filter function filters a sequence of elements based on a given predicate (a function that returns
 a boolean value) and returns a new sequence containing only the elements that meet the predicate.
  The filter function has the following syntax:

filter(predicate, iterable)
=>The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument.
The iterable argument can be a list, tuple, or any other iterable object.


"""
l=[1,2,3,4,3,4,56,65,55]
def filter_func(a):
    return a>4

new_list=list(filter(filter_func,l))
print(new_list)



# List of numbers
numbers = [1, 2, 3, 4, 5]

# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
print(list(evens))
# =>In the above example, the lambda function lambda x: x % 2 == 0 is used to filter the numbers list and
#     return only the even numbers. The filter function applies the lambda function to each element in the
#     list and returns a new list containing only the even numbers.
