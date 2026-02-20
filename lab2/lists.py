# list_example
#Python List:

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]
print(list1)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

"""
List--is a collection which is ordered and changeable. Allows duplicate members.
Tuple--is a collection which is ordered and unchangeable. Allows duplicate members.
Set--is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary--is a collection which is ordered** and changeable. No duplicate members.
"""

#Access List Items:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change List Items:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Add List Items:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")   #Insert at the end
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")    #To insert in specified place
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)   #Add "tropical" list to "thislist"
print(thislist)     

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)   #Add "thistuple" tuple to "thislist"
print(thislist)   

#Remove list items:

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")  #Remove first occurence of "banana"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)   #Remove item with index[1]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()   #Remove last item
print(thislist)  

thislist = ["apple", "banana", "cherry"]
del thislist    #Completely deletes all elements of list

#Loop Lists:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Sort Lists:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()   #Sort alphabetically
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()   #Sort numerically
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)  #Sort decreasing
print(thislist)

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)   #Sort the list based on how close the number is to 50
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)  #sort correctly
print(thislist)

#Copy Lists:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join Lists:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#List Methods:
""""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""





# list_exercise
fruits = ["apple", "banana", "cherry"]
print(fruits[1])   #return second(banana)

fruits = ["apple", "banana", "cherry"]
fruits[0]="kiwi"   #change apple to kiwi
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  #add orange to the end of list
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon") #insert lemon as the second element of list
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana") #remove banana from the list
print(fruits)

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])  #gets the last item

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])  #return third, fourth, and fifth element

fruits = ["apple", "banana", "cherry"]
print(len(fruits))