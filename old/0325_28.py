import re

s = input()

x = s.count("-")
y = s.count("_")

if x == y or y > x:
    s = re.sub("-", "_", s)
else:
    s = re.sub("_", "-", s)

print(s)