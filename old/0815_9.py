n, k, f = map(int, input().split())
l = [int(input()) for i in range(k)]

# print(n, k, f)
# print(l)

for i in range(f):
    l.pop(0)

l2 = []
for i in l:
    if i not in l2:
        l2.append(i)

for i in l2:
    print(i)
