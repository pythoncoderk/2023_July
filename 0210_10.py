n, y = map(int, input().split())
m = int(input())
l = list(map(int, input().split()))

# print(n, y)
# print(m)
# print(l)
x = 1
ok = 0
ng = 0
for i in range(m):
    if x >= n+1:
        x = 1
    if l[i] == x:
        ok += 1
        x += 1
    else:
        ng += 1
        x += 1
if ng >= y:
    print(-1)
else:
    print(ok * 1000)