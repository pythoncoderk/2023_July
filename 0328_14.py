l1 = list(map(int, input().split()))
l2 = [list(map(int, input().split())) for i in range(l1[0])]

# print(l1)
# print(l2)

max_l = l1[1]
for i in range(l1[0]):
    if l1[2] <= 0:
        break
    else:
        l1[1] += l2[i][0]
        l1[2] += l2[i][1]
    if max_l < l1[1]:
        max_l = l1[1]
print(max_l)
