n, s, p = map(int, input().split())

l = [list(map(int, input().split())) for i in range(n)]

# print(n, s, p)
# print(l)

l2 = []
for i in range(n):
    if s - p <= l[i][1] <= s + p:
        l2.append(l[i][0])
    else:
        l[i][0] = 0
if not l2:
    print("not found")
    exit()

max_l = max(l2)

for i in range(n):
    if l[i][0] == max_l:
        print(i + 1)
        exit()