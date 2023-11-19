import re

n = input()
x = re.findall(r"[_]", n)
y = re.findall(r"[-]", n)
if len(x) > len(y):
    print(re.sub("-", "_", n))
elif len(x) == len(y):
    print(re.sub("-", "_", n))
else:
    print(re.sub("_", "-", n))