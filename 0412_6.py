n, x, y = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, x, y)
# print(l)

if len(l) >= x:
    l.sort()
    for i in range(y):
        l.pop(0)
else:
    print(sum(l))
    exit()

if not l:
    print(0)
else:
    print(sum(l))