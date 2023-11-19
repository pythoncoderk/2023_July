import re

n = input()
n = re.sub("1", "A", n)
n = re.sub("2", "B", n)
n = re.sub("0", "C", n)
print(n)