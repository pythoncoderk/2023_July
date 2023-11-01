l = [1, 2, 3, 4, 5]
l2 = [int(input()) for i in range(4)]
x = 0
for i in range(len(l2)):
    if l[i] in l2:
        pass
    else:
        x += 1 + i
        break
print(x)