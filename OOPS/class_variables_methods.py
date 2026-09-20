class A:
    #Class variables
    member1 = "akash"
    member2 = "shivani"
    def __init__(self,a):
        self.a=a
    #Instance method
    def method1(self):
        self.member3=self.member2
        return self.member3
    def method2(self):
    #Variable inside a method can be accessed inside the other by using "self" keyword that unhides the current instance variable.
        return self.member2+"l",self.method1()
    #Static method
    @staticmethod
    def method3():
        return 6
    #Class method has 'cls' as the first parameter
    @classmethod
    def method6(cls):
        return (A.member1+'9')

    def __str__(self):
        print(self.a)

    def __repr__(self):
        print(self.a)

def main():

    #class variables/attributes can be accessed by classname or instance reference outside the class scope
    a=A(7)
    b=A(8)
    member1 = a.member1 * 2
    member2 = A.member2 * 2
    member3=a.method1()#Instance methods needs to be accessed with reference to a particular object/instance
    member4=a.method2()
   #Static methods can be accessed with reference to class name,which is not the case with instance method
    member5=A.method3()
    # Class methods can be accessed with reference to class name,which is not the case with instance method
    member6 = A.method6()
    print(member1, member2,member3,member4,member5,member6)


    # Changing a class variable using object, a new instance
    # ( or non-static) variable for that particular object is created and
    # this variable shadows the class variables.
    A.member1="akashi"
    print("New members\n",a.member1, b.member1)

    #Printing objects(__str__() and __repr__())
    print(a)
    #__str__() is called
    print([a])

class B:
    def method1(self):
        a=A()
        return (a.method1(),A.member1,A.member2)
if __name__ == '__main__':
    main()

b=B()
print(b.method1())