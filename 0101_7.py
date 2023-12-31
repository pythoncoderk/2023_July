n, s, p = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, s, p)
# print(l)

l2 = []
for i in range(n):
    if l[i][1] >= s - p and l[i][1] <= s + p:
        l2.append(l[i][0])
    else:
        l2.append(0)
max_l = max(l2)
if max(l2) == 0:
    print("not found")
else:
    print(l2.index(max_l) + 1)