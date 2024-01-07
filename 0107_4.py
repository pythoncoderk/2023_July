import re

s = input()
x = re.search(r"(\w*\.jpg|\w*\.png)", s)
print(x.start())