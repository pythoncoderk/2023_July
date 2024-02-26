import re

s = input()
x = re.search(r"CVE-[\d]{4}-.+", s)
print(x.start())