import re

n = int(input())
l = [input() for i in range(n)]
for i in l:
    if re.match("(([2][0-5][0-5]\.|[1][0-9][0-9]\.)|[0-9][0-9]\.|[0-9]\.)(([2][0-5][0-5]\.|[1][0-9][0-9]\.)|[0-9][0-9]\.|[0-9]\.)(([2][0-5][0-5]\.|[1][0-9][0-9]\.)|[0-9][0-9]\.|[0-9]\.)(([2][0-5][0-5]|[1][0-9][0-9])|[0-9][0-9]|[0-9])",
        i) != None:
        print(True)
    else:
        print(False)