import re

n = input()
print(re.search(r"p..za", n).start())

m = input()
print(re.search(r"p..za", m).start())