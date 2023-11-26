
# Dictionary Methods
# Dictionary uses several built-in methods for manipulation.They are listed below

# update()
# The update() method updates the value of the key provided to it if the item already exists in the dictionary,
# else it creates a new key-value pair.

#Example1:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)
#example 2
data1={'name':'ajay','age':20,'job':'teacher'}
data2={ 'address':'hyd','pin':500023}
data1.update(data2)
print(data1)

