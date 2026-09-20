#Even numbers

def even(num):
    if num<2:
        return (num%2==0)
    else:
        return even(num-2)
num=int(input("Enter number"))
if even(num)==True:
    print('Number %d is even'%num)
else:
    print(f'{num} is odd')

   


#Number of occurence of letter in word :

def check(string,ch):
      if not string:
        return 0
      elif string[0]==ch:
            return 1+check(string[1:],ch)
      else:
            return check(string[1:],ch)
string=input("Enter string:")
ch=input("Enter character to check:")
print("Count is:")
print(check(string,ch))


#Multiplying 2 numbers
def mult(m,n):
    if n==1:
        return m
    else:
        return (m+mult(m,n-1))

print(mult(3,4))

#Length of a list
# def length(L):
#     if not L:
#         return 0
#     else:
#         return 1+length(L[1:])
#
# print(length([6,4,5]))

#Sum of elements of a list
def sum(L):
    if not L:
        return 0
    else:
        return L[0]+sum(L[1:])
print(sum([6,4,5]))


#Binary search
search,L=5,[6,4,5]
def bin_search(L,ao,an):

    mid=(ao+an)//2
    # for i in range(len(L)):
    if search==L[mid]:
        return mid
    elif search<mid:
        return bin_search(L,ao,mid-1)
    elif search>mid:
        return bin_search(L,mid+1,an)

print(bin_search(L,0,len(L)-1))


#Insertion sort
def insertion_sort(l, k):
    if k > 1:
        insertion_sort(l, k - 1)
        insertion_logic(l, k - 1)
    return l


def insertion_logic(l, k):
    pos = k

    # for pos in range(len(l)):
    while pos > 0 and l[pos] < l[pos - 1]:
        l[pos], l[pos - 1] = l[pos - 1], l[pos]
        pos = pos - 1


l = [i for i in range(20, -1, -1)]
print(l)
print(insertion_sort(l, len(l)))





