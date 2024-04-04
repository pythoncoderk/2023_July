import re

s = input()

x = re.sub(r"a|A|e|E|i|I|o|O|u|U|", "", s)
print(x)