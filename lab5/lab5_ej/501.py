import re 

string = input()
match = re.match(r"^Hello", string)
print("Yes" if match else "No")
