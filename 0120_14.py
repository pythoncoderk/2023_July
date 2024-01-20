n = int(input())
l1 = [list(map(str, input().split())) for i in range(n)]
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]
for i in range(n):
    l1[i][1] = int(l1[i][1])
for i in range(n):
    l2[i][1] = int(l1[i][1])

d1 = {l1[i][0]: l1[i][1] for i in range(n)}
d2 = {l2[i][0]: l2[i][1] for i in range(m)}

print(d1)
print(d2)

print(d2[l1[0][0]])