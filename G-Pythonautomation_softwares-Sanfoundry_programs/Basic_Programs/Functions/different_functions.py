# #Default arguments
#
#
# def df(x=7,y=[]):
#     print(x,y)
#
#
# df(8, 'uyybu')
#
# def kw(x,y):
#     print(x,y)
# kw(x=9,y=8)
#
# def variable_len(*argv,**kwargs):
#     print(kwargs)
#     for k,v in kwargs.items():
#         print(k,":",v,end='  ')
#
# variable_len({'x':9,'y':8})
#
# cube=lambda x:x**3
# print('\n',cube(2))
#
import time
from functools import reduce
#
# start = time.time()
#
#
# def f1(list):
#     string = ""
#     for item in list:
#         string = string + chr(item)
#     return string
#
#
# print(f1([65, 66, 67]))
# print(time.time() - start)


def f2(lst):
    return reduce(lambda string, item: string+chr(lst), "", lst)


l = [65, 66, 67]
for i in l:
    print(chr(i))
print(f2([65, 66, 67]))
# print(time.time() - start)




