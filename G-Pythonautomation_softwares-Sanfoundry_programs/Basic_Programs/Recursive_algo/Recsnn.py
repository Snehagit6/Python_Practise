#Fibonacci
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Enter the range"))
for i in range(n):
    print(fibo(i))

l1 = []

#Python Program to Find the Sum of the Digits of the Number Recursively
def sum_digits(n):
    if n == 0:
        return 1
    dig = n % 10
    l1.append(dig)
    sum_digits(n // 10)


n = int(input("Enter the range"))
# for i in range(n):
#     print(fibo(i))

sum_digits(n)
print(sum(l1))

#Python Program to Find the GCD of Two Numbers Using Recursion

