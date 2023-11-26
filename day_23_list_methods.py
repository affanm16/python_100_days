"""
***List Methods*****
1)list.sort()
This method sorts the list in ascending order. The original list is updated

"""
#example 1
print("sort() method")
colors = ["violet", "indigo", "blue", "green","brown"]
colors.sort()
print(colors)

#example 2
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
"""
What if you want to print the list in descending order?
We must give reverse=True as a parameter in the sort method.
"""
#example 3
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

#example 4
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

#example 5
list1 = [10,20,100,100,30,50]
list1.sort(reverse=True)
print(list1)
#The reverse parameter is set to False by default.
#Note: Do not mistake the reverse parameter with the reverse method.
