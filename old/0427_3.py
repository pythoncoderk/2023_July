n = int(input())

l = [list(map(int, input().split())) for i in range(n)]

# print(l)

sort_l = sorted(l, key=lambda x: (x[0], x[1], x[2]), reverse=True)

for i in range(n):
    print(*sort_l[i])