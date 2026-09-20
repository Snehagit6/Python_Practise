l=[8,9,7,4]
list2=[]
#Bubble sort
for i in range(len(l)):
    for j in range(i+1,len(l)):
        # for descending less than and ascending greater than
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l[1])
#Bubble sort by recursion
sorted_l=[]
def rfunc(l):
    if len(l)<=1:
        return l
    elif l[0]>=l[1]:
        l[0],l[1]=l[1],l[0]
        return l[1:]

print("Recursive result",rfunc([9,8,6,7,7]))
#Insertion sort
a = [3, 1, 5, 2, 4]

for i in a[1:]:
    j = a.index(i)
    while j > 0 and a[j-1] > a[j]:
        a[j], a[j-1] = a[j-1], a[j]
        j = j - 1
