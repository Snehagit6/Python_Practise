list_1=[1,2,3,4]
list_2=[]
for l1 in range(len(list_1)+1):

    for l2 in range(l1+1,len(list_1)):
        list_2.append(list_1[l1:l2])


print([list_1[l1:l2] for l1 in range(len(list_1)+1) for l2 in range(l1+1, len(list_1)+1)])