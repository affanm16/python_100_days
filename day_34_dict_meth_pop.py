# pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

# popitem():
# The popitem() method removes the last key-value pair from the dictionary.

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

# del:
# we can also use the del keyword to remove a dictionary item.

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

#=> If key is not provided, then the del keyword will delete the dictionary entirely.

# # Example:
# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# del info
# print(info)

#making empty dictionary
ep1={}
print(ep1)