class Pair:
    def __init__(self, a1, b1):
        self.a1 = a1
        self.b1 = b1 
    def add (self, other):
        return f"Result: {self.a1 + other.a1} {self.b1 + other.b1}"
a1, b1, a2, b2 = input().split()
pair1 = Pair(int(a1), int(b1))
pair2 = Pair(int(a2), int(b2))

print(pair1.add(pair2))