import re

n = int(input())
l = [input() for i in range(4)]
l2 = []
for i in l:
    x = re.fullmatch("([2][0-5][0-5]|[1][\d][\d]|[\d][\d]|[\d])(\.[2][0-5][0-5]|\.[1][\d][\d]|\.[\d][\d]|\.[\d])+", i)
    if x == None:
        l2.append(False)
    else:
        y = len(i)
        z = x.span()[1]
        if y == z:
            l2.append(True)
        else:
            l2.append(False)
for i in l2:
    print(i)