
# ***Python - else in Loop****
# As you have learned before, the 'else' clause is used along with the if statement.

# Python allows the 'else' keyword to be used with the for and while loops too.
# The else block appears after the body of the loop.
# The statements in the else block will be executed after all iterations are completed.
# The program exits the loop only after the else block is executed.

# Syntax
# for counter in sequence:
#     #Statements inside for loop block
# else:
#     #Statements inside else block



# Example:
for i in range(5):#i takes values from 0 to 4
    print(i)
else:
    print("i is 5 now")

#example2:
for i in range(10):
    print(i)
    if(i==4):
        break;#break will end the loop
else:
    print("it will not break for loop but ends for loop,else will not get printed")

#example2:while-else loop
n=0
while n<10:
    print(n)
    n=n+1;
    if(n==5):
        break#break will end the loop
else:
    print("else is not used here")
