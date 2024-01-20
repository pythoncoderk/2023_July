import re

s = input()
s = re.sub(r"A", "4", s)
s = re.sub(r"E", "3", s)
s = re.sub(r"G", "6", s)
s = re.sub(r"I", "1", s)
s = re.sub(r"O", "0", s)
s = re.sub(r"S", "5", s)
s = re.sub(r"Z", "2", s)

print(s)