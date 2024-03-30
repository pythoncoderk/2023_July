import re

s = input()

s = re.sub("0", "*", s)
s = re.sub("1", "+", s)
s = re.sub("\*", "1", s)
s = re.sub("\+", "0", s)

print(s)
