import re

n = int(input())
s = input()

s = re.sub("a", "#", s)
s = re.sub("b", "*", s)

if s.count("#*") == 0 and s.count("*#") == 0:
    print("No")
else:
    print("Yes")
