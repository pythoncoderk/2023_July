ab, ac, bc = map(str, input().split())

a = 0
b = 0
c = 0

if ab == "<":
    b += 1
else:
    a += 1

if ac == "<":
    c += 1
else:
    a += 1

if bc == "<":
    c += 1
else:
    b += 1

l = [["A",a], ["B", b], ["C", c]]
l = sorted(l, key=lambda k: k[1])

print(l[1][0])