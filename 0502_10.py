import re

s = input()

x = re.sub(r"a|e|i|o|u|A|E|I|O|U", "", s)
print(x)