"""
the range fuctioon returns a sequence of numbers starting from 0 by default
 and increments by 1(default) and stops before a specified number
 syntax- range(start,stop,step)

START:optional,integer specifying at which position to start,default is 0
STOP: required,position to stop(excluding the num)
STEP:optional,incrementation,default is 1

"""



#type 1
for i in range(5):
    print(i)#want to print from 1 take k=k+1

#type 2

for k in range(1,20,2):#increment by 2
    print(k)#prints from 1 to 8