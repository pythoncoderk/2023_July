n, x, y = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, x, y)
# print(l)

l.sort()
if len(l) >= x:
    for i in range(y):
        l[i] = 0

print(sum(l))

