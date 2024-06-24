import re
x = input()
x = re.fullmatch(r"([\d][\d][\d]|[\d][\d]|[\d])\.([\d][\d][\d]|[\d][\d]|[\d])\.([\d][\d][\d]|[\d][\d]|[\d])\.([\d][\d][\d]|[\d][\d]|[\d])", x)
print(x)