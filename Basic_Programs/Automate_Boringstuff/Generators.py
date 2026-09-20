x = [8, 9, 7]
g = (i ** 2 for i in x)  # Generator expression
print(next(g))


def gen_fun(a, r):
    for i in a:
        if i < 50:
            yield i
            i += r # yield stops the iteration
            yield r
#Generator function returns a generator object.
a = (gen_fun([2,6], 10))

# def cg():
#     g = (x + 5 for x in range(5))  # Generator expression
#     l = [x + 5 for x in range(5)]
#     s = iter(l)
#     print(next(s))
#     print(next(s))
#     print(next(s))
#     print(next(g))
#
#     print(next(g))


print(next(a))
print(next(a))

def fib_gen(n):
    a,b=0,1
    while(a<n):
        yield a
        a,b=b,a+b


try:
    n=int(input("Enter the occurence"))

except:
    raise ValueError()

for i in fib_gen(n):
    print(i)




def factorial_gen(num):
    num = 4
    factorial = 1
    for i in  range(1,num+1):
        yield factorial
        factorial=factorial*i


for j in factorial_gen(4):
    print(i)

# Iterators
# Iterators
# are
# objects
# that
# can
# be
# iterated
# upon.
# Python
# uses
# the
# __iter__()
# method
# to
# return an
# iterator
# object
# of
# the
#
#
# class .
#     The
#     iterator
#     object
#     then
#     uses
#     the
#     __next__()
#     method
#     to
#     get
#     the
#     next
#     item.
#
#
# for loops stops when StopIteration Exception is raised.
# filter_none
# edit
# play_arrow
#
# brightness_4
#
#
# # This program will reverse the string that is passed
# # to it from the main function
# class Reverse:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index -= 1
#         return self.data[self.index]
#
#
# def Main():
#     rev = Reverse('Drapsicle')
#     for char in rev:
#         print(char)
#
#
# if __name__ == '__main__':
#     Main()
# Output:
#
# e
# l
# c
# i
# s
# p
# a
# r
# D
# Generators
# Another
# way
# of
# creating
# iterators.
# Uses
# a
# function
# rather
# than
# a
# separate
#
#
# class
#     Generates
#     the
#     background
#     code
#     for the next() and iter() methods
#
#
# Uses
# a
# special
# statement
# called
# yield which
# saves
# the
# state
# of
# the
# generator and set
# a
# resume
# point
# for when next() is called again.
# filter_none
# edit
# play_arrow
#
# brightness_4
#
#
# # A Python program to demonstrate working of Generators
# def Reverse(data):
#     # this is like counting from 100 to 1 by taking one(-1)
#     # step backward.
#     for index in range(len(data) - 1, -1, -1):
#         yield data[index]
#
#
# def Main():
#     rev = Reverse('Harssh')
#     for char in rev:
#         print(char)
#     data = 'Harssh'
#     print(list(data[i] for i in range(len(data) - 1, -1, -1)))
#
#
# if __name__ == "__main__":
#     Main()