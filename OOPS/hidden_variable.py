class A:
    __hiddenelem=9
    def add(self,i):
        self.__hiddenelem=7
        print(self.__hiddenelem+i)
    def square(self,s):
        print(self.__hiddenelem**2)
a=A()
a.add(7)
a.square(2)
# print(a.__hiddenelem)
print(a.A.__hiddenelem)

