from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# enumerate
for i, value in enumerate(nums, start=1):
    print("Index:", i, "Value:", value)

# zip
letters = ["a", "b", "c", "d", "e", "f"]
for n, ch in zip(nums, letters):
    print(n, ch)

# type checking and conversion
text = "100"
number = int(text)
print(number, type(number))
print(isinstance(number, int))