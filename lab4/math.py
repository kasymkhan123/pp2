# Write a Python program to convert degree to radian.
"""
Input degree: 15
Output radian: 0.261904
"""
from math import *
n = int(input())
print("Input degree:", n)
print("Output radian:", radians(n))

# Write a Python program to calculate the area of a trapezoid.
"""
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
"""
h = int(input())
b1 = int(input())
b2 = int(input())

print("Height:", h)
print("Base, first value:", b1)
print("Base, second value:", b2)
A = ((b1+b2)/2)*h
print("Expected Output:", A)

# Write a Python program to calculate the area of regular polygon.
"""
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""
import math
n = int(input("number of sides:"))
a = int(input("length of a side:"))
s = a*a*n*(1/4)*(math.tan((math.pi)*(n-2)/(2*n)))
print(round(s))

# Write a Python program to calculate the area of a parallelogram.
"""
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0
"""
b = int(input())
h = int(input())
A = b * h
print("Length of base:", b)
print("Height of parallelogram:", h)
print("Expected Output:", A)