import re

n = input()
x = re.findall(r"[0]{3}|[1]{3}|[2]{3}|[3]{3}|[4]{3}"
                r"|[5]{3}|[6]{3}|[7]{3}|[8]{3}|[9]{3}", n)
if len(x) != 0:
    print("Yes")
else:
    print("No")