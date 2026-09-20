a = float(input("Enter the 1rst number"))
b = float(input("Enter the 2nd number"))
print(f"Before swapping : a:{a},b:{b}")
a, b = b, a
print(f"After 1rst swapping : a:{a},b:{b}")
a = (a+b)
b = a-b
a = a-b
print(f"After 2nd swapping : a:{round(a,2)},b:{round(b,2)}")





