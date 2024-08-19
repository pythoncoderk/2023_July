import re

s = input()

x = re.sub("ZONe", "*", s)
print(x.count("*"))