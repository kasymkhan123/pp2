#Python Variables

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.

#Get the Type:
x = 5
y = "John"
print(type(x))
print(type(y))

# Single or Double Quotes:
x = "John"
x = 'John' # "" same as '' 

# Case-Sensitive:
a = 4
A = "Sally" #A will not overwrite a

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

'''
Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
'''
# Camel Case
myVariableName = "John"
# Pascal Case
MyVariableName = "John"
# Snake Case
my_variable_name = "John"

# Many Values to Multiple Variables:
# Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Global Variables:
# exampl1:
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

# exampl2:
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

# The global Keyword, example1:
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

#example12:
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)