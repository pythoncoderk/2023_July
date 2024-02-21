n, x, y = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, x, y)
# print(l)

l.sort(reverse=True)
# print(l)

if len(l) >= x:
    for i in range(y):
        l.pop()

print(sum(l))