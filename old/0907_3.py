n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

x = 0
y = 0

for i in range(n - 1):
    if len(l[x]) > y:
        x = l[x][y] - 1
    else:
        x = l[y][x] - 1
    y += 1

print(l[x][y] if len(l[x]) > y else l[y][x])