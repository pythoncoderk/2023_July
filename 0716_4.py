l = list(map(int, input().split()))
n = int(input())
l2 = [list(map(str, input().split())) for i in range(n)]

for i in range(n):
    for j in range(len(l2[i])):
        if j != 0:
            l2[i][j] = int(l2[i][j])

print(l)
print(n)
print(l2)

