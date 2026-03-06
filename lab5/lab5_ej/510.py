import re 

text = input()
pattern = re.search(r"(cat|dog)", text)

print('Yes' if pattern else "No")