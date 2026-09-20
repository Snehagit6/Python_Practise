num=int(input("Enter the number"))
fact=1
#Normal approach
# while(num>0):
#     fact=fact*num
#     num=num-1
# print("Factorial",fact)
#With recursion
def fact_rec(num):
    while(num<=1):
        return 1
    else:
        return num*fact_rec(num-1)
print("Factorial is %d"%fact_rec(num))

# Alternate recursion
def fact(num):
    fact=1
    fact=num*1
    while(num<=1):

        fact=num*fact(num-1)

print("ALternative way",fact(6))