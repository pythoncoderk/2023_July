import re

a, b = map(int, input().split())

l = [str(i) for i in range(a, b+1)]
# print(l)

l2 = l[::]
# print(l2)

l3 = []
for i in range(len(l2)):
    x = ""
    for j in range(len(l2[i])):
        if l2[i][j] == "6":
            x += "s"
        elif l2[i][j] == "9":
            x += "n"
        else:
            x += l2[i][j]
    x = re.sub("s", "9", x)
    x = re.sub("n", "6", x)
    x = x[::-1]
    l3.append(x)
# print(l3)
count = 0
for i in range(len(l3)):
    if "2" not in l3[i] and "3" not in l3[i] and "4" not in l3[i] and "5" not in l3[i] and "7" not in l3[i]:
        if l3[i] == l[i]:
            count += 1
print(count)
