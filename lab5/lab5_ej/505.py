import re

string = input()
pattern = re.search(r"^[a-zA-Z]+[0-9]$", string)

print("Yes" if pattern else "No")