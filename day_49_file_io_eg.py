f=open("file1.txt",'a')#it creates file and appends it without deleting the previous content
f.write("hello!this is affan")
f.close()
f=open("file1.txt",'r')
text=f.read()
print(text)