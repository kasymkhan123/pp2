# Create a generator that generates the squares of numbers up to some number N.

def generator(n):
    for i in range(1, n+1):
        yield i**2

makeSquares = generator(5)
for i in range(5):
    print(next(makeSquares))

#Write a program using generator to print the even numbers 
#between 0 and n in comma separated form where n is input from console.
def evens(n):
    for i in range(0, n+1):
        if i%2==0:
            yield i

n=int(input())
my_nums=evens(n)
print(list(my_nums))

# Define a function with a generator which can iterate the numbers, 
# which are divisible by 3 and 4, between a given range 0 and n.
def num(n):
    for i in range(0, n+1):
        if i%3==0 and i%4==0:
            yield i
        
divisible = num(100)
for i in range(9):
    print(next(divisible))

# Implement a generator called squares to yield the square of all numbers from (a) to (b). 
# Test it with a "for" loop and print each of the yielded values.
def squares_inrange(a, b):
    for i in range(a, b+1):
        yield (i*i)

squares = squares_inrange(2, 10)
for i in range(2, 11):
    print(next(squares))

# Implement a generator that returns all numbers from (n) down to 0.
def returning(n):
    for i in range(n+1, -1, -1):
        yield i

ret = returning(9)
for i in range(11):
    print(next(ret))