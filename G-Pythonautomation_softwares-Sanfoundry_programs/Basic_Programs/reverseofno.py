n = int(input("Enter the number of elements to be reversed:"))

rev = 0
while n > 0:
    dig = n % 10
    rev = rev*10+dig
    n = n//10
print("Reversed number : ", rev)




