import re

n = int(input())
l = [input() for i in range(n)]

for i in range(n):
    x = re.fullmatch(r"(2[0-5]{,2}|1\d{2}|\d{1,2})\.{3}(2[0-5]{,2}|1\d{2}|\d{1,2})", l[i])
    if x is None:
        print(False)
    else:
        print(True)