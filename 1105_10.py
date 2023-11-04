n = list(input())
n.sort()
x = 0
for i in range(4):
    if n.count(n[i]) >= 2:
        x += 1
if x >= 1:
    print("NG")
else:
    print("OK")