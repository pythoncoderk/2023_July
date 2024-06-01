n = int(input())
l = list(map(int, input().split()))
m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]
x = 0
l_result = []
for i in range(n):
    x += l[i]
    l_result.append(x)
l_result.insert(0, 0)

print(n)
print(l)
print(m)
print(l2)
print(l_result)

for i in range(m):
    y = l_result[l2[i][1] - (l2[i][0] - 1)]
    