import numpy as np
import webbrowser
n = np.array([4,5,6,7])
print(n)

print(n*n)
print(n-n)
print(1/n)
print(n**3)
arr=np.arange(0,11)
arr[0:4]=100#Setting the first 3 numbers in array as a constant value:100
print(arr)
list=[1,5,8,7,5]
try:
    list[0:3]=4
    print(list)
except Exception as e:
    print("Difference between list and ndarray,for list: ",e.args)

# array=np.zeros([10][10])


arr1 = np.arange(50).reshape((10,5))
arr2=arr1.T
print(arr1,arr2)

arr=np.arange(11)
print(np.sqrt(arr))
print(np.exp(arr))

A=np.random.randn(10)
B=np.random.randn(10)
print(np.add(A,B))
print(np.maximum(A,B))

webbrowser.open("https://www.udemy.com/")

