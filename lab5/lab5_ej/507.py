import re 

text = input()
pattern = input()
replacement = input()

new_text = re.sub(pattern, replacement, text)
print(new_text)
