import random
# random module is used to generate random numbers
# randint() method used to genrate random integers between two numbers(inclusive)
# print(random.randint(0,4))

user =int(input(" input your choice\n 0 for snake,1 for water and -1 for gun\n"))
comp=random.randint(-1,1)
print("you:",user)
print("computer:",comp)
def check(comp,user):
 if(comp==user):
     return 0 #no points
 if(comp==0 and user ==1):
     return -1 # -1 point
 if(comp==1 and user==-1):
     return -1
 if(comp==-1 and user==0):
     return -1
 return 1 #else user wins..give 1 point

score= check(comp,user)#check functioon 
if(score==0):
    print("its draw")
elif(score==-1):
    print("you loose")
else:
    print("you won")
