#readlines()method
# reads a single line from the file
# multiple lines can be read using loops
"""
f = open('file1.txt','r')
while True:
    line=f.readline()
    print(line)
    if not line:
        break
"""

#example2
f=open('file1.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"marks of student {i} in maths is: {m1}")
    print(f"marks of student {i} in english is: {m2}")
    print(f"marks of student {i} in sst is: {m3}")
    print(line)

#***writelines() method
#=>the writelines()method in python writes a sequence of strings to a file.the sequence can be any iterable object
#     ,such as list or a tuple
#example1
f=open('myfile2.txt','w')
lines=['apple\n','orange\n','mango\n']
# print(lines)
f.writelines(lines)
f.close()