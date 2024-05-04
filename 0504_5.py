import re

a, b = map(int, input().split())

# print(a, b)

l = [str(i) for i in range(a, b+1)]
# print(l)

count = 0
for i in range(len(l)):
    x = l[i]
    x = re.sub("6", "S", x)
    x = re.sub("9", "N", x)
    x = re.sub("S", "9", x)
    x = re.sub("N", "6", x)
    x = x[::-1]
    if len(x) == 1:
        if x == "0" or x == "1" or x == "8":
            count += 1
    else:
        if "2" not in x and "3" not in x and "4" not in x and "5" not in x and "7" not in x:
            if x == l[i]:
                count += 1
print(count)