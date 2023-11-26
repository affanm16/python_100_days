"""
***II. intersection and intersection_update()****:
=>The intersection() and intersection_update() methods prints only items that are similar to both the sets.
=>The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
"""
# Example:intersection() method
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.intersection(cities2)
print(cities3)
print(cities1)
print(cities2)#1 and 2 do not get changed

# Example :intersection_update()
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities1.intersection_update(cities2)
print(cities1)#cities 1 gets updated