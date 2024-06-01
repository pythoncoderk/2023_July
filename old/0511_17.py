a = [1, 5, 9, 7, 5, 3, 2, 5, 8, 4]
a_l = []
x = 0
for i in range(len(a)+1):
    if i == 0:
        a_l.append(0)
    else:
        x += a[i-1]
        a_l.append(x)
print(a_l)

