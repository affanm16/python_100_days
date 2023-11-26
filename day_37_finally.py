
# Finally Clause
# The finally code block is also a part of exception handling.
# When we handle exception using the try and except block, we can include a finally block at the end.
# The finally block is always executed, so it is generally used for doing the concluding tasks like
# -closing file resources or closing database connection or may be ending the program execution with a delightful message.

"""Syntax:
try:
   #statements which could generate
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to
    #execute in any situation
The finally block is executed irrespective of the outcome of try……except…..else blocks
One of the important use cases of finally block is in a function which returns a value.
"""
# Example1:
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")


#example2
def func1():
    try:
        list=[1,5,6,7]
        i=int(input("enter the index:"))
        print(list[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:#instead of finally if there is any statements ,it will not execute after try/except block
        #here though the  function returns at try/expect but also finally block is executed
        print("i am always executed")
x=func1();
print(x)