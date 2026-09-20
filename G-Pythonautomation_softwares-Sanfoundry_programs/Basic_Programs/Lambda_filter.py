from collections import Counter

def split_odd_even(l):
    return{'even':list(filter(lambda n :(n%2==0),l)),'odd':list(filter(lambda n:(n%2!=0),l))}

print(split_odd_even([10, 13, 16, 22, 9, 4,37]))

#lambda functions

x=lambda a:a+10
print(x(7))
#Lambda function can take another function as argument
def function(n):
    return lambda a:a**n

square=function(4)
cube=function(4)

print(square(2),' ',cube(3))
#Quadratic functions
def quadratic_func(a,b,c):
    return lambda x:a*x**2+b*x+c
f=quadratic_func(2,3,4)
print(f(3))

my_list = ["geeks", "geeg", "keek", "madam", "practise"]
rev_list=list(filter(lambda a:(a=="".join(reversed(a))),my_list))#For palindrome use reversed and for anagram
# use Counter
print(rev_list)

#Combining first and last name
name=lambda x,y:x.strip().title()+" "+y.strip().title()
print(name("sneha","mazumder"))

#Anonymous function with no input
message=lambda:"This is nice!"

authors=["Aurther Conan Doyle","H.G Wells","Anton Chekhov"]
authors.sort(key=lambda x:x.split(" ")[-1].lower())
print(authors)


