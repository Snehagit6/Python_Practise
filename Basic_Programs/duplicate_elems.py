l = [9,8,8,7,6,6]
s = set(l)
l_d = []
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] == l[j]:
            l_d.append(l[i])
print(l_d)

nd = [l[i]for i in range(len(l)) for j in range(i+1,len(l))if l[i]==l[j]]
print(nd)

list4=[]
if list4[(len(list4))]==None:
    print("list4 is empty")
