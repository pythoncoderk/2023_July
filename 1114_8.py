import re

n = input()
print(re.search(r"\\\(\^ \. \^\)/", n).start())