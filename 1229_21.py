import re

n = input()
n = re.sub(r"A", "100", n)
n = re.sub(r"B", "111", n)

print(n)