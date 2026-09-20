#P1:
k = 'hello'

def explode(k):

    if len(k)<=1:
        return k
    else:
        return k[0]+' '+explode(k[1:])

print(explode(k))

#Alternative
l=(' ').join([i for i in k])
print(l)

#P2:
l="aabbbc"
def func(string):
    if len(string)<=1:
        return string
    elif string[0]==string[1]:
        return func(string[1:])
    else:
        return string[0]+func(string[1:])

print(func(l))

#Alternative:Removing duplicate elements from a list
lu=[i for i in l]
ko=[]
for j in range(len(lu)):
    for k in range(j+1,len(lu)):

        if l[j]==l[k]:
            if l[k] not in ko:
                ko.append(l[k])
# for c in l:
#     if c not in ko:
#             ko.append(c)

print(ko)

