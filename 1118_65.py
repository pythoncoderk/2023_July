import re

s = input()
x = re.fullmatch("[2][\d][\d]", s)
y = re.fullmatch("[4][\d][\d]", s)

if x != None:
    print("ok")
elif y != None:
    print("error")
else:
    print("unknown")