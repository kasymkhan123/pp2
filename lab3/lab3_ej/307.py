import math
class Point :
    def __init__(self, x, y, other_x, other_y):
        self.x = x 
        self.y = y
        self.other_x = other_x
        self.other_y = other_y
    def show(self) :
        print("({}, {})".format(self.x, self.y))
    def move(self, new_x, new_y):
        self.new_x = new_x
        self.new_y = new_y
        print("({}, {})".format(self.new_x, self.new_y))
    def dist(self):
        distance = math.sqrt((self.other_x-self.new_x)**2 + (self.other_y - self.new_y)**2)
        return distance 

x, y = input().split()
new_x, new_y = input().split()
other_x, other_y = input().split()

point = Point(int(x), int(y), int(other_x), int(other_y))
point.show()
point.move(int(new_x), int(new_y))

dist = point.dist()

print(f"{dist:.2f}")




