#extend():This method adds an entire list or
# any other collection datatype (set, tuple, dictionary) to the existing list.

#Example 1:
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)



#Concatenating two lists:
#You can simply concatenate two lists to join two lists.

#Example2
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
