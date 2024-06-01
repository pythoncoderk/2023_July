n, c = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, c)
# print(l)

l2 = []
total = 0
for i in range(n):
    if total + l[i][1] > c:
        break
    if l[i][0] <= 10:
        l2.append(l[i][0])
        total += l[i][1]
    else:
        total += l[i][1]
    if total > c:
        break
if len(l2) >= 10:
    print("Yes")
else:
    print(len(l2))