n, s, p = map(int, input().split())

# print(n, s, p)
x = 1
l = []
while x <= n:
    l1 = []
    for i in range(s):
        if x > n:
            break
        else:
            l1.append(x)
            x += 1
    l.append(l1)
xxx = len(l)
if p > xxx:
    print("none")
else:
    print(*l[p-1])

