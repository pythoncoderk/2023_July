n, m = map(int, input().split())
l = [input() for i in range(m)]

# print(n, m)
# print(l)

ng = []
for i in range(n):
    ng.append(l.pop())

ng = set(ng)
l = set(l)

print(len(l - ng))