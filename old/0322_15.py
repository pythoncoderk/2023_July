n, v = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, v)
# print(l)

count = 0
for i in range(n-1):
    x = l[i+1][0] - l[i][0]
    y = l[i+1][1] - l[i][1]
    total = y / x
    if total >= v:
        count += 1
if count >= 1:
    print("YES")
else:
    print("NO")

