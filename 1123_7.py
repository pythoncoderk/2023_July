import re

s = input()
s = re.sub("A", "4", s)
s = re.sub("E", "3", s)
s = re.sub("G", "6", s)
s = re.sub("I", "1", s)
s = re.sub("O", "0", s)
s = re.sub("S", "5", s)
s = re.sub("Z", "2", s)
print(s)