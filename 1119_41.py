import re

x, y = map(str, input().split())
z = x + y
m = re.fullmatch(r"[1]{2,4}|[2]{2,4}|[3]{2,4}|[4]{2,4}|[5]{2,4}"
                 r"|[6]{2,4}|[7]{2,4}|[8]{2,4}|[9]{2,4}", z)
if m != None:
    print('Yes')
else:
    print("No")