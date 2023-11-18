import re

s = input()
s = re.sub("True", "False", s)
s = re.sub("False", "True", s)
print(s)