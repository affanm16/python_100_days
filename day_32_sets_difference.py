# IV. difference() and difference_update():
# =>The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets.
# The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

#Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

#Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))

