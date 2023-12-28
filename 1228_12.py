import re

s = input()

s = re.sub("0", "C", s)
s = re.sub("1", "A", s)
s = re.sub("2", "B", s)

print(s)
