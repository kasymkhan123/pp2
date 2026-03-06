import re 

text = input()
two_more_digits = re.findall(r"\d{2,}", text)

print(" ".join(two_more_digits))