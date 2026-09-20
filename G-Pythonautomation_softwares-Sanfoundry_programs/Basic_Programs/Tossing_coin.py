import random as rand
sides=['head','tail']
count=dict.fromkeys(sides,0)
for i in range(4):
    side=rand.choice(sides)
    count[side]+=1
print(count)


name='aabbb'
print(len(name))

for i in range(len(name)):
    if(i%2==0):
        print(name[:i])
    
