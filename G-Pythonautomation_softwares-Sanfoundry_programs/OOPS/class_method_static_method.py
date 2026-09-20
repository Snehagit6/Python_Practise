def s1(x, y):
    return x*y

class A:

    @staticmethod
    def s1(x, y):
        return x + y

    def s2(self, x, y):
        return s1(x, y)

a = A()
# print(a.s2(3, 7))
# from abc import ABC, abstractmethod
#
# class A(ABC):
#
#     @abstractmethod
#     @classmethod
#     def m1(self):
#         print('In class A, Method m1.')
#
# class B(A):
#
#     @classmethod
#     def m1(self):
#         print('In class B, Method m1.')
#
# b = B()
# b.m1()
# B.m1()
# A.m1()

from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # A class method to create a Person object by birth year.Class method takes cls as the 1rst args
    # and can access and change the state of the class
    @classmethod
    def fromBirthYear(cls,name, year):
        return cls(name, (date.today().year - year))

    # a static method to check if a Person is adult or not.Static method donot take any args
    #     # and cannot access and change the state of the class
    @staticmethod
    def isAdult(age):
        age=age+2
        return age
               # > 18
    def method1(self):
        name=self.name+"dia"

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

# print (person1.age)
# print (person2.age)

# print the result
print (Person.isAdult(22))
print(person1.age)
print(person2.age)
