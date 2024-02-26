import re

s = input()
x = re.sub(f"raw_input", "input", s)
print(x)