l1=[i for i in 'aeiou']
k='+'.join(l1).split('+')
print(isinstance(k,list))
s='jko1234'
str1=[]
int1=[]
for i in s:
    if(i.isalpha()):
        str1.append(i)
    elif(i.isnumeric()):
        int1.append(i)
print(str1)
print(int1)
print("\'b'")