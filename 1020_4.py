import copy
import re

n = input()
m = copy.copy(n)

cal1 = []
n = list(n)
while len(n) != 0:
    if n[0] == "+" or n[0] == "-":
        cal1.append(n.pop(0))
    else:
        n.pop(0)
ml = re.split("[+-]", m)

x = int(ml[0])
ml.pop(0)
while len(cal1) != 0:
    if cal1[0] == "+":
        cal1.pop(0)
        x = x + (int(ml[0]))
        ml.pop(0)
    else:
        cal1.pop(0)
        x = x - (int(ml[0]))
        ml.pop(0)

print(x)


