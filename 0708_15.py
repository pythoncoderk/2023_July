n, x, p = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, x, p)
# print(l)

l.append(x)
l.append(p)

l.sort()
print(l.index(p) + 1)