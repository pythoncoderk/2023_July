n = int(input())

l = [list(map(str, input().split())) for i in range(n)]

# print(l)

for i in range(n):
    l[i][1] = int(l[i][1])

l_f = sorted(l, key=lambda k: k[1], reverse=True)

print(l_f[1][0])
