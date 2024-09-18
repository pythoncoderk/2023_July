l = []
for i in range(1, 100 + 1):
    if 100 % i == 0:
        l.append(i)

chk = False
a, b = map(int, input().split())
for i in range(a, b + 1):
    if i in l:
        chk = True
        break

print("Yes" if chk else "No")