import math
class Circle :
    def __init__(self, radius):
        self.radius = radius
    def area (self, pi = 3.14159):
        return pi * (self.radius**2)

r = int(input())
area = Circle(r)
print(f"{area.area():.2f}")