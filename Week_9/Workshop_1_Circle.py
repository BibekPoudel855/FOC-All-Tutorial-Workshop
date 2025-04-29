class Circle :
    diameter = None
    radius = None
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * (self.radius**2)

c = Circle(4)
print("Area : ", c.area())