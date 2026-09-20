# def outer(x, y):
# 
#     def inner1():
#         return x+y
# 
#     def inner2(z):
#         return inner1() + z
# 
#     return inner2
# 
# 
# f = outer(10, 25)
# 
# print(f(15))

def outer(x, y):

    def inner1():
        return x+y

    def inner2():
        return x*y

    return (inner1, inner2)


(f1, f2) = outer(10, 25)

print(f1())
print(f2())