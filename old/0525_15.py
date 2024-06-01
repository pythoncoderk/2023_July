n, t = map(int, input().split())
l = list(map(int, input().split()))

print(n, t)
print(l)

l2 = []
x = 1
for i in range(n):
    l3 = []
    for j in range(n):
        l3.append(x)
        x += 1
    l2.append(l3)

print(l2)

for i in range(n):
    for j in range(n):
        