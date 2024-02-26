import re

s = input()
x = re.search(r".?(\.jpg|\.png)", s)
print(x.start())