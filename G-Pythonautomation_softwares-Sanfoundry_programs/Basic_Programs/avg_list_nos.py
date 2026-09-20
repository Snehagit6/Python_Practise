n = int(input("Enter the number of elements to be inserted:"))
list = []
sum = 0
for i in range(0, n):
    e = int(input("Enter the element"))
    list.append(e)
    sum = sum+e


def result():
    print(f"List of range{n} : ",list)
    print(f"Sum of all elements in {list} : ",sum)
    print(f"Average of all elements in {list} : ",round(sum/n,1))




