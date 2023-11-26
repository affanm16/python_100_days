"""
****'is' vs '==' in Python****
=>In Python, is and == are both comparison operators that can be used to check if two values are equal.
    However, there are some important differences between the two that you should be aware of.

=>The 'is' operator compares the identity of two objects, while the' == 'operator compares the values of the objects.
 This means that 'is' will only return 'True' if the objects being compared are the exact same object in memory,
  while '==' will return True if the objects have the same value.
"""
# For example:

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True-compares the exact location of object in memory
print(a is b)  # False-compares values
# =>In this case, a and b are two separate lists that have the same values, so' ==' returns True.
    #However, a and b are not the same object in memory, so is returns False.

# =>One important thing to note is that, in Python, strings and integers are immutable, which means
    #   that once they are created, their value cannot be changed. This means that, for strings and integers,
    #'is' and' ==' will always return the same result:

a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5
# here,as a,b are immutable that is once a is created and 5 is stored for b it will not allocate another
# memory space,but it will will just make it point to a as both have same values
print(a == b)  # True
print(a is b)  # True


# In these cases, a and b are both pointing to the same object in memory, so is and == both return True.
# For mutable objects such as lists and dictionaries, is and == can behave differently.
# In general, you should use == when you want to compare the values of two objects, and use is when you
# want to check if two objects are the same object in memory.
