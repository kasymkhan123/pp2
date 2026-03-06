import re

text = input()
pattern = input()

literal_pattern = re.escape(pattern)

matches = re.findall(literal_pattern, text)

print(len(matches))