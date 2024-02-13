import re

x = input()
l = [str(i) for i in range(0, 365)]
# print(l)
count = 0
for i in l:
    xxx = re.search(x, i)
    if xxx is not None:
        count += 1
print(count)