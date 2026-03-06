import re 

text = input()
count_word_pattern = re.findall(r"\b\w+\b", text)

print(len(count_word_pattern))