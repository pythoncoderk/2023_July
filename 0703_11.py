n, v = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, v)
# print(l)

count = 0
for i in range(n - 1):
    x = l[i + 1][0] - l[i][0]
    y = l[i + 1][1] - l[i][1]
    if y / x >= v:
        count += 1

print("YES" if count >= 1 else "NO")