import re 

person = input()
pattern = re.compile(r"Name: ([a-zA-Z ']+), Age: (\d+)")
match = pattern.search(person)

print(match.group(1), match.group(2))