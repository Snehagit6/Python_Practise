#Sorting helps in binary search

l = [2,7,19,34,53,72]

def selection_sort(l):

    for i in range(len(l)):
        min = 0
        for j in range(i+1, len(l)):
            if l[j]<l[min]:
                min=i
        l[i], l[min] = l[min], l[i]
    return l

print(selection_sort(l))