import re 

text = input()
new_text = re.findall(r"\b[a-zA-Z]{3}\b", text)

print(len(new_text))