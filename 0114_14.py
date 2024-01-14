n = int(input())
l = [0, 2, 4, 6, 8]
l2 = []
x = 0
while len(l2) < n:
    l_num = 0
    y = str(x)
    l3 = list(y)

    if "1" in l3 or "3" in l3 or "5" in l3 or "7" in l3 or "9" in l3:
        l_num = 1
        x += 2
    else:
        l2.append(x)
        x += 2
print(l2[-1])