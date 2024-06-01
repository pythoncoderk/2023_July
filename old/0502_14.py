n, a, b = map(int, input().split())
l = [list(input()) for i in range(a)]

# print(n, a, b)
# print(l)

for i in range(n):
    x = l[0].pop(0)
    if l[1]:
        if x == l[1][0]:
            y = l[1].pop(0)
    if l[2]:
        if x == l[2][0]:
            y = l[2].pop(0)

print(f"{len(l[1])} {len(l[2])}")
