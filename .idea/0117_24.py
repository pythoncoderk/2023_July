import re

s = input()
x = re.sub(r"(\d{2})\.(\d{2})", r"\1/\2", s, 1)
print(x)