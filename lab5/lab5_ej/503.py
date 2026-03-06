import re 

s1 = input()
s2 = input()

pattern_mathes = re.findall(s2, s1)
print(len(pattern_mathes))