class A:
    private_var = 5
    __private_var = 4

    def __init__(self):
        self.p = 10

    def public_m(self):
        print("Public")

    def private_m(self):
        return self.__private_m()

    def __private_m(self):
        print("Private")
        return A.__private_var

a = A()
print(a.p)

