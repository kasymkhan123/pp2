import re

s1 = input()
s2 = input()

if re.search(s2, s1) :
    print("Yes")
else :
    print("No")