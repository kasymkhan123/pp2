import re

text = input()
date = re.findall(r"\d{2}/\d{2}/\d{4}", text)

print(len(date))