# # # Python function to print permutations of a given list
# # def permutation(lst):
# #     # If lst is empty then there are no permutations
# #     if len(lst) == 0:
# #         return []
# #
# #         # If there is only one element in lst then, only
# #     # one permuatation is possible
# #     if len(lst) == 1:
# #         return [lst]
# #
# #         # Find the permutations for lst if there are
# #     # more than 1 characters
# #
# #     l = []  # empty list that will store current permutation
# #
# #     # Iterate the input(lst) and calculate the permutation
# #     for i in range(len(lst)):
# #         m = lst[i]
# #
# #         # Extract lst[i] or m from the list.  remLst is
# #         # remaining list
# #         remLst = lst[:i] + lst[i + 1:]
# #
# #         # Generating all permutations where m is first
# #         # element
# #         for p in permutation(remLst):
# #             l.append([m] + p)
# #     return l
# #
# #
# # # Driver program to test above function
# # data = list('123')
# # print("Data",data)
# # for p in permutation(data):
# #     print(p)
# #
# # x='*'
# # n=5
# # for j in range(n):
# #     for i in range(n-j):#range(j)
# #
# #         print(x,end='')
# #     print('\n')
#
l2=[-1,-2,2,1,1,3,1]
n=len(l2)
l3=[]
for i in range(len(l2)-2):
    # if l2[i]==0:
    #     print([l2[i]])
    for j in range(i+1,len(l2)-1):
        # print(j)
        # if(l2[i]+l2[j]==0):
        #     print([l2[i],l2[j]])
        for k in range(j+1,n):
            # if (l2[i]+l2[i+1:][j]+l2[j+1:][k]==0):
                if l2[i]+l2[j]+l2[k]==0:

                    l3.append([l2[i],l2[j],l2[k]])
            # for m in range(len(l2[k+1:])):
            #     if(l2[i]+l2[j]+l2[k]+l2[m]==0):
            #         l3.append([l2[i], l2[j], l2[k],l2[m]])
print(l3)


#Premutation of a list[Recursion:returns output at once and generator:yields output when called]
def perm(lst):
    if len(lst)==0:
        yield []
    elif len(lst)==1:
        yield lst
    else:

        for each in range(len(lst)):
            x=lst[each]
            xs=lst[:each]+lst[each+1:]
            for p in perm(xs):
                yield [x]+p

for p in perm([1,2,3]):
    print(p)



