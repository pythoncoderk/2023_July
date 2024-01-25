l = list(map(str, input().split()))
# print(l)
l.sort(reverse=True)
total = []
for i in range(4):
    l2 = l[::]
    for j in range(3):
        a = l2.pop(i)
        b = l2.pop(j)
        c = l2.pop(0)
        d = l2.pop(0)
        x = a + b
        y = c + d
        total.append(int(x) + int(y))
        l2 = l[::]
print(max(total))
