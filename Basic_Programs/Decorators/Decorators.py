# '''P:1'''
# # def outer(func):#higher oder function:outer ->>takes another function as an argument
# #     def inner():
# #         print("Accessing :",func.__name__) 
# #         return func()
# #     return inner
# #  
# # # def greet():
# # #     print("Hello")
# # # wish=outer(greet)#wish->closure function.
# # # wish()#wish when called,inner function gets executed
# # 
# # #Decorating greet
# # # greet=outer(greet)#decorator function name:@outer greet=outer(greet)->>@outer
# # # greet()
# # 
# # @outer
# # def greet():
# #     print( "Hello!")
# # greet()
# 
# 
# '''P:2'''
# class A:
# 
#     def __init__(self, val):
#         self.x = val
# 
#     @property
#     def x(self):
#         return self.__x
# 
#     @x.setter
#     def x(self, val):
#         self.__x = val
#         
#     @x.deleter
#     def x(self):
#         del self.__x
# 
# a = A(7)
# del a.x
# print(a.x)

def log(func):
    def inner(input):
        print("Accessed the function:", func.__name__ )
        print(input)
        return func(input)
    return inner
@log       
def greet(msg):
    """

    :param msg:
    """
    print('Greeting Message : ' +msg)

greet("Welcome!")
