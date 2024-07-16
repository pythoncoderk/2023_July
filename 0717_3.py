h, w = map(int, input().split())
r, c = map(int, input().split())

# print(h, w)
# print(r, c)

count = 0
l = []
for i in range(1, h + 1):
    l2 = []
    for j in range(1, w + 1):
        l2.append(i)
        l2.append(j)
        l.append(l2)
        l2 = []

for i in range(len(l)):
    x = l[i][0]
    y = l[i][1]

    ans1 = abs(x - r)
    ans2 = abs(y - c)

    if ans1 + ans2 == 1:
        count += 1

print(count)