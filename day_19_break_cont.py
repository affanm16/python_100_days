"""
***break statement***
The break statement enables a program to skip over a part of the code.
 A break statement terminates the very loop it lies within.
"""
#example for break
for i in range(21):
    print("5*",i,"=",5*i)
    if(i==10):
        break



"""
****Continue Statement*****
The continue statement skips the rest of the loop statements and causes the next iteration to occur.
"""
#example for continue

for i in range(11):
    if(i==2):
        print("skipping the iteration")
        continue
    print("5*",i,"=",5*i)
