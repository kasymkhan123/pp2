import re 

string = input()
pattern = re.search(r"\S+\@\S+\.\S+", string)

print(pattern.group() if pattern else "No email")