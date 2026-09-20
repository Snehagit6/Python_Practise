class A:
    def call(self):
        print("Call A")
class B:
    def call(self):
        print("Call B")
class C:
    def call(self):
        print("Call C")

class D(A,B,C):
    def call_func(self):
        self.call()

    def base_class(self):
        print(self.__class__.__bases__)
    #Solution of diamond problem:which method to invoke.The ordering of base classes defines the order of search
    def restructure(self,p1,p2,p3):
        self.__class__.__bases__ = (p1, p2, p3)

d=D()

d.base_class()
d.restructure(B, A, C)
d.call_func()

#MRO
print(D.__mro__)
print(D.mro())

