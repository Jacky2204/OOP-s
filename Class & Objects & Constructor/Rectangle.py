# Create a Rectangle class:
# length, width
# Method: area()
# Method: perimeter()

class Rectangle:
    def __init__(self,length, width):
        self.length=length 
        self.width=width 
        
    def area(self):
        print(f"Area of Rectangle is {self.length * self.width}")
        
    def perimeter(self):
        print(f"Perimeter of Rectangle is {2*(self.length + self.width)}")
        
        
a=Rectangle(2,3)
a.area()
a.perimeter()