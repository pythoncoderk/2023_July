n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

a = []
for i in range(n):
    if l[i][0] == 1:
        a.append(l[i][1])
    else:
        x = l[i][1] * -1
        print(a[x])
