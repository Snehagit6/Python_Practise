def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)


# User defined polymorphic functions

def add(x,y,z=0):
    print(x+y+z)

add(8,7)
add([9,0],[8],[3])


