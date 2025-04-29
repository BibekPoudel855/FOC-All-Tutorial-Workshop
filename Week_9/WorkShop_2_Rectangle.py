class Rectangle :
    length = None
    breadth = None
    def __init__(self, length, breadth) :
        self.length = length
        self.breadth = breadth

    def area(self) :
        return self.length * self.breadth
    
    def perimeter(self) :
        return 2 * (self.length + self.breadth)
    

r = Rectangle(2, 2)
print("Area  : ", r.area())
print("Perimeter : ", r.perimeter())


r1  = Rectangle(20, 10)
print("Area : ", r1.area())
print("Perimeter : ", r1.perimeter())