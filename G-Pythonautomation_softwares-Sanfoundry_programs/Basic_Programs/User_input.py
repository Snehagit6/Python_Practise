Input_1=['Yes','No']
Input_2=[1,2]
Input_3=['ck','sk']
input1=input("Enter the first input")
if input1 in Input_1:
    input2=int(input("Enter the second input"))
    if input2 in Input_2:
        input3=input("Enter the third input")
        if input3 not in Input_3:
            print("Enter the correct third input")
            
    else:
        print("Enter the correct second input")
    
else:
    print("Enter the correct first input")

x,y,z=((input("Enter numbers"))).split()
print(x,y,z)