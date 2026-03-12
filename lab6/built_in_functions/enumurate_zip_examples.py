from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# map
doubled = list(map(lambda x: x * 2, nums))
print("Doubled:", doubled)

# filter
odds = list(filter(lambda x: x % 2 == 1, nums))
print("Odds:", odds)

# reduce
sum_all = reduce(lambda a, b: a + b, nums)
print("Sum:", sum_all)