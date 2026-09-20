# When we pass a reference and change the received reference to something else,
#  the connection between passed and received parameter is broken.


def func(x):

    x = x*3
    return x


y = 5
print(func(y))
print(y)