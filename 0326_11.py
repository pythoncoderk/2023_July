import re

s = input()

s = re.sub(r"a|e|i|o|u", "", s)
print(s)