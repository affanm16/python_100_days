def avg(*numbers):
    sum=0
    for i in numbers:
        sum =sum+i
        return (sum/len(numbers))
c= avg(10,20,100)
print(c)