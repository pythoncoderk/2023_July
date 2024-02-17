n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])

# print(n)
# print(l)

x = sorted(l, key=lambda x: x[1], reverse=True)
print(x[1][0])