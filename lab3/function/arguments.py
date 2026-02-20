#1
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#2
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")
#3
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#4 
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")
#5 
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")
#6
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
#7
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")
#8
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)
#9
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
#10
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)
#11
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)
#12
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])
#13
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)
#14
def my_function(name, /):
  print("Hello", name)

my_function("Emil")
#15
def my_function(name):
  print("Hello", name)

my_function(name = "Emil")
#16
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")
#17
def my_function(name):
  print("Hello", name)

my_function("Emil")
#18
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)