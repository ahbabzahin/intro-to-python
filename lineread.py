file=open("abc.txt","r")
print(file.readline())
file.close()

file=open("abc.txt","a")
file.write("this is a new line")
file.close()