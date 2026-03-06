import re 

text = input()
upper_case_pattern = re.findall(r"[A-Z]", text)

print(len(upper_case_pattern))