n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

l2 = []
for i in range(n):
    x = l[i][0] + l[i][1]
    y = 24 - l[i][2]
    l2.append(x + y)
# print(l2)
print(min(l2))
print(max(l2))