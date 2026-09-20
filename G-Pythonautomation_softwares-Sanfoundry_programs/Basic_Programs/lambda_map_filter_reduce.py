l=[(7,9),(1,2),(8,7)]
l.sort(key=lambda x:x[0])
print(l)


#Mapping a function to each element in a list

z=[("Austria",35),("Belgium",42),("Canada",32),("London",34)]
f=lambda x:(x[0],round((9/5)*x[1]+32,2))
print(list(map(f,z)))

d={"Sneha":"Maz","Zanet":"Jith"}
# k=[k for k in d]
# v=[v for v in d.values()]
# v.sort()
# # print(k)
# # v=[d[i] for i in k]
# k = [k for k,v in zip(k,v) if d[k]==v ]
# print(k)
# print(f"Sorted dict{dict(zip(k,v))}")
print(sorted(d.items(),key=lambda x:x[1]))

countries=["","Argentina","Brazil","Canada",""]
print(list(filter(None,countries)))






