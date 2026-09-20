def collatz(num):
    try:

        if num % 2 == 0:
            print(num, "is even")
        else:
            print(num, "is odd")
    except:
        raise ValueError
print("Enter number")
collatz(int(input()))
m=[8,9,10]
import pprint as pp
p = pp.pformat(m)
print(p)
