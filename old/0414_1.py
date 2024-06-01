import re

a, b = map(int, input().split())

# print(a, b)

l = [str(i) for i in range(a, b+1)]
# print(l)

count = 0
for i in range(len(l)):
    x = re.search(r"2|3|4|5|7", l[i])
    if x is None:
        xx = l[i]
        xx = re.sub("6", "==", xx)
        xx = re.sub("9", "@@", xx)

        xx = re.sub("==", "9", xx)
        xx = re.sub("@@", "6", xx)

        if l[i] == xx[::-1]:
            count += 1

print(count)

