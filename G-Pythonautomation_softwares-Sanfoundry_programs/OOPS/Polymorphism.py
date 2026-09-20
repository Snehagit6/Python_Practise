# User defined polymorphic functions

def add(x,y,z=0):
    print(x+y+z)

add(8,7)
add([9,0],[8],[3])

class A:
    def ops(self,a,b):
        return a+b
class B:
    def ops(self,a,b):
        return a*b

def func(obj):
    return obj.ops(7,8)

print(func(B()))
