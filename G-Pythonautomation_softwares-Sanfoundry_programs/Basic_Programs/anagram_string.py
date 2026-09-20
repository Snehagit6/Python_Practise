a="gardener"
b="danger"
# l=[t if (len(a)==len(b))  for  t in a if t not in b ]
c=[]

if (len(a)==len(b)):
    for t in a:
        if t not in b:
           c+=[t]

else:
    print('a :{a} and b :{b} are not anagrams'.format(a=a, b=b))

