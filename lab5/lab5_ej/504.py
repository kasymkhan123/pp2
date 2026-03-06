import re

string = input()
pattern_digits = re.findall(r"\d", string)

print(*pattern_digits)