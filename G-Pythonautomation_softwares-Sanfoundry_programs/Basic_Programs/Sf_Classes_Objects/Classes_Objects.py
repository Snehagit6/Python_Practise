# Python Program to find the area of a rectangle using classes.


class Area():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        area=self.length*self.breadth
        return area
a=Area(int(input("Enter length : ")),int(input("Enter breadth : ")))
print("Area :",a.area())
    
        