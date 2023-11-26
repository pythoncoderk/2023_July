a, b, n = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
# print(a, b, n)
# print(l)
l2 = []
for i in range(n-1):
    x = l[i+1][0] - l[i][1]
    if a * 2 < x * b:
        y = a * 2
    else:
        y = x * b
    l2.append(y)
print(sum(l2) + (a * 2))
