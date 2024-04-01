n, y = map(int, input().split())
m = int(input())
l = list(map(int, input().split()))

# print(n, y)
# print(m)
# print(l)

x = 1
count = 0
ng = 0
for i in range(m):
    if ng >= y:
        print(-1)
        exit()
    if x > n:
        x = 1
    if l[i] == x:
        count += 1
        x += 1
    else:
        ng += 1
        x += 1
print(count * 1000)
