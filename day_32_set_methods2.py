

#***Set Methods***
#There are several in-built methods used for the manipulation of set.They are explained below

# isdisjoint():if there is no common it returns true
# The isdisjoint() method checks if items of given set are present in another set.
# This method returns False if items are present, else it returns True.

# Example:
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities1.isdisjoint(cities2))

# issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set.
# It returns True if all the items are present, else it returns False.

# Example:
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities1.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities1.issuperset(cities3))


# issubset():
# The issubset() method checks if all the items of the original set are present in the particular set.
# It returns True if all the items are present, else it returns False.

# Example:
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities1))

# add()
# If you want to add a single item to the set use the add() method.

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

# update()
# If you want to add more than one item, simply create another set or
# any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

# remove()/discard()
# We can use remove() and discard() methods to remove items form list.

# Example :
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

# =>The main difference between remove and discard is that, if we try to delete an item which is not present in set,
# then remove() raises an error, whereas discard() does not raise any error.

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)

# pop()
# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered.
# However, you can access the popped item if you assign the pop() method to a variable.

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# del
# del is not a method, rather it is a keyword which deletes the set entirely.

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)

# =>What if we don’t want to delete the entire set, we just want to delete all items within that set?

# clear():
# This method clears all items in the set and prints an empty set.

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)


# Check if item exists
# You can also check if an item exists in the set or not.

# Example
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")


