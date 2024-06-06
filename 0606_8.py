n, d = map(int, input().split())
x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, d)
# print(x, y)
# print(l)

count = 0
for i in range(n):
    answer = abs(x - l[i][0]) + abs(y - l[i][1])
    if answer <= d:
        count += 1

print(count)