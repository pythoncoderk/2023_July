import re

n = "255.255.255.255"
x = re.match(r"[0-2][0-5][0-5]\.[0-2][0-5][0-5]\.[0-2][0-5][0-5]\.[0-2][0-5][0-5]", n)
if x != None:
    print(True)
else:
    print(False)