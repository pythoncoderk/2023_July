n = int(input())

l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

l_f = sorted(l, key=lambda x: (x[0], x[1], x[2]), reverse=True)
# print(l_f)

for i in range(n):
    print(*l_f[i])