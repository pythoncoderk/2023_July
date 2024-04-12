n, c = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, c)
# print(l)

l2 = []
total = 0
count = 0
for i in range(n):
    if total + l[i][1] <= c:
        if l[i][0] <= 10:
            count += 1
            total += l[i][1]
            l2.append(l[i][0])
        else:
            total += l[i][1]
    else:
        break
if len(l2) == 10:
    print("Yes")
else:
    print(count)
