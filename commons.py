#
# >>> any([1>0,1==0,1<0])
# True
# >>> any([1<0,2<1,3<2])
# False
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())
# l = input().split()
# print(all([int(i)>0 for i in l]) and any([i==i[::-1] for i in l]))

d1, d2 = {'A' : 1,'B':3},{'A':4,'B':3}

print(any([d1['A']==d2['A']]))