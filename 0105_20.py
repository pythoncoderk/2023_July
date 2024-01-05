x, y, z = map(int, input().split())
l = []
while l == []:
    if x % y == z:
        l.append(x)
    else:
        x += 1
print(*l)