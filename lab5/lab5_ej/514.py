import re 

text = input()
pattern = re.compile(r"\b\d+\b")

print("Match" if pattern.search(text) else "No match")