a, b = map(int, input().split())
c, d = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

# print(a, b)
# print(c, d)
# print(l1)
# print(l2)

x = []

if l1[a-1] > l1[b-1]:
    x.append(b)
else:
    x.append(a)

if l1[c-1] > l1[d-1]:
    x.append(d)
else:
    x.append(c)

x.sort()
# print(x)

if l2[0] > l2[1]:
    print(x[1])
    print(x[0])
else:
    print(x[0])
    print(x[1])