import re 

def double(digit) :
    num = str(digit.group())
    num += num
    return num

digit = input()
double_pattern = re.sub(r"\d", double, digit)

print(double_pattern)
