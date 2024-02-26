import re

s = input()
x = re.search(r"database_.{,5}\.db", s)
print(x.start())