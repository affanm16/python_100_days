"""
*Function Arguments and return statement

There are four types of arguments that we can provide in a function:

1)Default Arguments
2)Keyword Arguments
3)Variable length Arguments
4)Required Arguments


****Default arguments:
We can provide a default value while creating a function.
This way the function assumes a default value even if a value is not provided in the function call for that argument.


*Keyword arguments:
We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name.
Hence,the order in which the arguments are passed does not matter.


*Required arguments:
In case we don’t pass the arguments with a key = value syntax,
then it is necessary to pass the arguments in the correct positional order and
the number of arguments passed should match with actual function definition.



***Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function.
This can be done using variable-length arguments.

There are two ways to achieve this:

1)Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function.
The function accesses the arguments by processing them in the form of tuple.

Example:

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")
Output:

Hello, James Buchanan Barnes

2)Keyword Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function.
The function accesses the arguments by processing them in the form of dictionary.

Example:

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")
Output:

Hello, James Buchanan Barnes


*******return Statement
The return statement is used to return the value of the expression back to the calling function.

Example:

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))
Output:
"""
#default arguement
def average(a=9,b=1):
    print("the average is",+(a+b)/2)

#calling the function
average()#even if we dont provide the arguements it will take the default value i.e 9,1

#keyword Arguements

average(b=9,a=11)#order dosn't matter

#Required arguements
def avg(a,b,c):
    print("average is",(a+b+c)/2)

avg(10,20,30)

#Arbitary Arguements
def avg1(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is:", (sum)/len(numbers))
avg1(5,6,7,1)#you can add as many as no.s it takes it as a tuple
"**"will be used if parameters are dictionary