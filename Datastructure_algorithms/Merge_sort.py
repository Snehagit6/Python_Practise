#Sorting helps in binary search

l = [2,73,89,4,0]

def insertion_sort(l):

    for i in range(len(l)):
        min_pos =i
        while min_pos>0 and l[min_pos]<l[min_pos-1]:

            l[min_pos],l[min_pos-1]=l[min_pos-1],l[min_pos]
            min_pos=min_pos-1
    return l

print(insertion_sort(l))