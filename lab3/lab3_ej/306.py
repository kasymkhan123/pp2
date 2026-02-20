class Shape ():
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Rectangle (Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area (self):
        return self.length * self.width

length, width = input().split()

area = Rectangle(int(length), int(width))
print(area.area())