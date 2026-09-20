lm=[7,8,[1,2],[5,6],[8,9]]
s=0
for i in lm:
    if (type(i)==list):
        for j in i:
            s=s+j
    else:
        s=s+i

print(s)


string="element"
dict={}
for k in string:
    if k in dict.keys():
        c = 1
        dict[k]=c+1
    else:
        dict[k]=1
print(dict)


