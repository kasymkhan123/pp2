import re 

string = input()
re_delimiter_pattern = input()

new_string = re.split(re_delimiter_pattern, string)
print(",".join(new_string))