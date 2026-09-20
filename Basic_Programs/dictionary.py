# d1={'k1':1,'k2':3,'k3':8}
# d2={'k1':4,'k2':3,'k3':8}
# match_d={}
# for k1 in d1.keys():
#     if k1 in d2.keys():
#         if d1[k1]==d2[k1]:
#             match_d[k1]=d1[k1]
# print(match_d)
#
# kj={k1:d1[k1]for k1 in d1.keys()if k1 in d2.keys()if d1[k1]==d2[k1]}
# print(kj)

my_dict = {'a': 123, 'b': {'c' :[1, 4, 5, 7], 'k': (1, 3 ,5)},'n': {"p": '', 'x': 56,'g':[], 'find': ''},'url': ''}

null_string=[]
for k1,v1 in my_dict.items():
    if isinstance(v1,dict):
        for k2,v2 in v1.items():
            if v2=='':
                null_string.append([k1,k2])

# null_string.append(k2)



    else:
        if v1=='':
            null_string.append(k1)


for j in null_string:
    if isinstance(j,list):
        del my_dict[j[0]][j[1]]
    else:
        del my_dict[j]



print(my_dict)