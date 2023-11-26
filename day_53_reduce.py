"""

***reduce****
=>The reduce function is a higher-order function that applies a function to a sequence and returns a single value.
    It is a part of the functools module in Python and has the following syntax:

    reduce(function, iterable)

=>The function argument is a function that takes in two arguments and returns a single value.
    The iterable argument is a sequence of elements, such as a list or tuple.

=>The reduce function applies the function to the first two elements in the iterable and then applies the function
    to the result and the next element, and so on. The reduce function returns the final result.



"""
from functools import reduce
list2=[1,2,3,4,5]
"""
1+2=3
3+3=6
6+4=10
10+5=15
"""
sum=reduce(lambda x,y:x+y,list2)
print(sum)
"""
=>In the above example, the reduce function applies the lambda function lambda x, y: x + y to the elements
in the numbers list. The lambda function adds the two arguments x and y and returns the result.
 The reduce function applies the lambda function to the first two elements in the list (1 and 2),
  then applies the function to the result (3) and the next element (3), and so on. The final result is
  the sum of all the elements in the list, which is 15.

=>It is important to note that the reduce function requires the functools module to be imported in order to use it.
"""
