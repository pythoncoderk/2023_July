n, s, p = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
# print(l)
l2 = []
for i in range(n):
    if s - p <= l[i][1] <= s + p:
        l2.append(l[i][0])
    else:
        l2.append(0)
# print(l2)
max_l = max(l2)
if len(l2) == l2.count(0):
    print("not found")
else:
    for i in range(len(l2)):
        if l2[i] == max_l:
            print(i + 1)
            break