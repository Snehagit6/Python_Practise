l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[1,4,7],[2,5,8],[3,6,9]]
l=[]
l2_=[]
# for k in range(len(l1)):
#     n=[elem for elem in l1[k] if l1[k].index(elem)==k]
#     for i in l1:
#         for j in i:
#             if i.index(j)==k:
#                 if j not in l1[k]:
#                     n.append(j)
#                     n.sort()
#
#     #Reverse=True ->arranging array in descending order.
#     list.append(n)

# for each in range(0,len(l1)):
#     lst = []
#     for i in l1:
#
#         lst.append(i[each])
#     l.append(lst)



print([[i[each] for i in l1] for each in range(len(l1))])






