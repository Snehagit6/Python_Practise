import string

n="Sneha Maz"
print(n[len(n)-1::-1])
#
# s='ABCDCDCCEFCDCCDC'
# st="CDC"
# count=0
# for each in range(len(s)):
#
#         h=s[each:each+(len(st))]
#         if st in h:
#             count+=1
# print(count)
# from functools import reduce
# lis=[[9,8,7],[9,6,7],[9,7,7]]
# lis2=[2,9,8,7]
# max=0
# for i in range(len(lis2)):
#     for j in range(i+1,len(lis2)):
#         max_p=lis2[i]*lis2[j]
#         if max_p>max:
#             max=max_p
#             max_t=(lis2[i],lis2[j])
#
# print(max_t)
#
# list2=[reduce(lambda x,y:x*y,i)for i in lis]
#
# max=list2[0]
# max_pos=0
# for each in range(len(list2)):
#     if list2[each]>max:
#         max=list2[each]
#         max_pos=each
#
# print(list2,lis[max_pos])


#position of substring in string
#
# k="This is Python"
# sk='is'
#
# i=0
# pos_l=[]
# while(i<len(k)):
#     pos=k.find(sk,i,len(k))
#     if pos!=-1:
#         i=i+1
#         pos_l.append(i)
#     else:
#         i=i+1
#
# print(pos_l)


#Remove nth index character from a non-empty string
s="This is a Correct Code"
index=8
print(s[:index]+'the'+s[index+1:])

#Find out if 2 strings are anagrams
s1="garden"
s2="ardentiou"
flag=True
if len(s1)==len(s2):
    list1=[i for i in s1 if i not in s2]
    if not list1:
        print("Two strings are anagram")
    else:
        print("Two strings are not anagram")

else:
    print("Two strings are not anagram")
s_=list(s1)
for i in range(len(s_)):
    for j in range(i+1,len(s_)):
        if s_[i]>s_[j]:
            s_[i],s_[j]=s_[j],s_[i]
print("Sorted string s1: ",''.join(s_))

#First & last characters exchanged

print(s1[-1]+s1[1:-1]+s1[0])

#Num vowels

vowels=['a','e','i','o','u']
l=[]
c=0
for i in s2:
    if i in vowels:
        c+=1
        l.append(i)
print("Number of vowels in s2:",c,l)

# Take in a String and Replace Every Blank Space with Hyphen
print(s.replace(" ","-"))

print('-'.join(s.split()))

# Python Program to Calculate the Length of a String Without Using a Library Function
c_=0
for i in s1:
    c_+=1
print(f"length of {s1} :{c_}")

# Python Program to Remove the Characters of Odd Index Values in a String
s1__=""
for each in range(len(s1)):
    if each%2==0:
        s1__=s1__+s1[each]
print("String",s1__)

# Python Program to Calculate the Number of Words and the Number of Characters Present in a String
print("Num of words",len(s.split()))
char_num=0
for each in (s.split()):
    char_num+=len(each)
print(char_num)
char=0
word=1
for i in s:
      char=char+1
      if(i==' '):
            word=word+1
print(char,word)
# Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
# s1_=input("Enter string1")
# s2_=input("Enter string2")
# c1=0
# c2=0
# for i in s1_:
#     c1+=1
# for j in s2_:
#     c2+=1
# if c1>c2:
#     print("s1_ is larger")
# elif c1==c2:
#     print("Equal")
# else:
#     print("s2_ is smaller")
# Python Program to Count Number of Lowercase Characters in a String
c_lower=0
for i in s:
    if i.islower():
        c_lower+=1

print(c_lower)
# Python Program to Check if a String is a Palindrome or Not
s1_=""
for i in range((len(s1)-1),-1,-1):

    s1_=s1_+s1[i]
if s1_==s1:
    print("Palindrome")
else:
    print("Not plaindrome")


# Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String
c_lower_=0
c_upper_=0
for i in s:
    if i.islower():
        c_lower_+=1
    elif i.isupper():
        c_upper_+=1
print(c_lower_,c_upper_)
# Python Program to Check if a String is a Pangram or Not

# Python Program to Accept a Hyphen Separated Sequence of Words as Input and Print the Words in a Hyphen-Separated Sequence after Sorting them Alphabetically
hs="This-is-cool"
ls=hs.split('-')
print(ls)
ls.sort()
print(ls)

# Python Program to Calculate the Number of Digits and Letters in a String
nls="This is 2 good"
digit=0
letters=0
for each in nls:
    if each.isdigit():
        digit+=1
    elif each>='a' and each<='z' or each>='A' and each <='Z':
        letters+=1
print(digit,letters)

# Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String
c=0
for i in nls:
    c+=1
print(nls[:2]+nls[c-2:])
# Python Program to Count the Occurrences of Each Word in a Given String Sentence
spl=s.split()
d={}

for each in spl:
    for each_ in range(len(s)):
        h=s[each_:each_+len(each)]
        if each in h:
            d[each]=d.get(each,0)+1
print(d)
# Python Program to Check if a Substring is Present in a Given String
string="Python Programramm"
substring="ram"
pos=string.find(substring,0,len(string))
print(string.find(substring,pos+1,len(string)))
# Python Program to Print All Permutations of a String in Lexicographic Order without Recursion

# Python Program to Print All Permutations of a String in Lexicographic Order using Recursion
from math import factorial


def print_permutations_lexicographic_order(s):
    """Print all permutations of string s in lexicographic order."""
    seq = list(s)
    for _ in range(factorial(len(seq))):
        print(''.join(seq))
        nxt = get_next_permutation(seq)
        # if seq is the highest permutation
        if nxt is None:
            # then reverse it
            seq.reverse()
        else:
            seq = nxt


def get_next_permutation(seq):
    """Return next greater lexicographic permutation. Return None if cannot.

    This will return the next greater permutation of seq in lexicographic
    order. If seq is the highest permutation then this will return None.

    seq is a list.
    """
    if len(seq) == 0:
        return None

    nxt = get_next_permutation(seq[1:])

    # if seq[1:] is the highest permutation
    if nxt is None:
        # reverse seq[1:], so that seq[1:] now is in ascending order
        seq[1:] = reversed(seq[1:])

        # find q such that seq[q] is the smallest element in seq[1:] such that
        # seq[q] > seq[0]
        q = 1
        while q < len(seq) and seq[0] > seq[q]:
            q += 1

        # if cannot find q, then seq is the highest permutation
        if q == len(seq):
            return None

        # swap seq[0] and seq[q]
        seq[0], seq[q] = seq[q], seq[0]

        return seq
    else:
        return [seq[0]] + nxt

#
# s = input('Enter the string: ')
ls=list(s)
ls_r=ls[::-1]
f_l=[]
def permutation(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            l[i],l[j]=l[j],l[i]
            f_l.append(''.join(l))


# permutation(ls)
# permutation(ls_r)
# print(f_l,len(f_l))
# print_permutations_lexicographic_order(s)


from math import factorial


def print_permutations_lexicographic_order(s):
    """Print all permutations of string s in lexicographic order."""
    seq = list(s)

    # there are going to be n! permutations where n = len(seq)
    for _ in range(factorial(len(seq))):
        # print permutation
        print(''.join(seq))

        # find p such that seq[p:] is the largest sequence with elements in
        # descending lexicographic order
        p = len(seq) - 1
        while p > 0 and seq[p - 1] > seq[p]:
            p -= 1

        # reverse seq[p:]
        seq[p:] = reversed(seq[p:])

        if p > 0:
            # find q such that seq[q] is the smallest element in seq[p:] such that
            # seq[q] > seq[p - 1]
            q = p
            while seq[p - 1] > seq[q]:
                q += 1

            # swap seq[p - 1] and seq[q]
            seq[p - 1], seq[q] = seq[q], seq[p - 1]


# s = input('Enter the string: ')
# print_permutations_lexicographic_order(s)


def permute_string(str):
    if len(str) == 0:
        return ['']

    prev_list = permute_string(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list

print(permute_string('ABCD'))

#Alternative:
def permutation(word):
    if len(word) == 1:
        return [word]
    perm = permutation(word[1:])
    char = word[0]
    r = []

    for p in perm:

        for i in range(len(p) + 1):
            r.append(p[:i] + char + p[i:])
    return r


print(permutation('ABAAC'))


stringpos="This is beautiful"
occ=0
each=0
while each<len(stringpos):
    k=stringpos.find('is',each,len(stringpos))
    if k!=-1:
        occ+=1
        print(k)
        each=k+1

    else:
        pass
letter = string.ascii_lowercase
print(letter)


# For duplicate characters in a string, always try dictionary approach where keys cannot eb duplicate.