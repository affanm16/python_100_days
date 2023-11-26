"""
***Joining Sets****
=>Sets in python more or less work in the same way as sets in mathematics.
=>We can perform operations like union and intersection on the sets just like in mathematics.

***I. union() and update()****:
=>The union() and update() methods prints all items that are present in the two sets.
=>The union() method returns a new set whereas update() method adds item into the existing set from another set.
"""
# Example:union()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)


# Example:update()
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities1.update(cities2)
print(cities1)
