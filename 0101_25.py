n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][0] = int(l[i][0])

# print(n)
# print(l)
l.sort()
for i in range(n):
    print(f"{l[i][0]} {l[i][1]}")