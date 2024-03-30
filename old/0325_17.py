import re

n = input()
out_s = ""
for i in range(len(n)):
    x = re.match(f"\d", n[i])
    if x is not None:
        out_s += n[i]
print(out_s)
