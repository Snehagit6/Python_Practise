class A:

    def public_m(self):
        print("Public")

    def private_m(self):
        return self.__private_m()

    def __private_m(self):
        print("Private")

a = A()
print(a.private_m())
