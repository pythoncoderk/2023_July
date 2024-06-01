n, y = map(int, input().split())
m = int(input())
l = list(map(int, input().split()))

# print(n, y)
# print(m)
# print(l)

count = 1
total = 0
ng = 0
while l:
    if count > n:
        count = 1
    x = l.pop(0)
    if count == x:
        total += 1000
        count += 1
    else:
        ng += 1
        count += 1
if ng >= y:
    print(-1)
else:
    print(total)