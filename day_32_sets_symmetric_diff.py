"""
***III. symmetric_difference and symmetric_difference_update()***:
=>The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets.
=>The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
=>symmetric A-B=(A◡B)-(A◠B)
"""
# Example:
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.symmetric_difference(cities2)
print(cities3)
# Example:
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities1.symmetric_difference_update(cities2)
cities2.symmetric_difference_update(cities1)
print(cities1)
