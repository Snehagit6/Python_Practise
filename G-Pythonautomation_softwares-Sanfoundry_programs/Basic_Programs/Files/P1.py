#Python Program to Read the Contents of a File
f1=open("./File_read.txt",'w+')
line=f1.readline()
l=0
while line!="":
    print(line)
    l+=1
    if "T" in line:
        print(line)
    line=f1.readline()
print("Number of lines",l)
f1.close()

