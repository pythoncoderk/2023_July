l = list(map(str, input().split()))
# print(l)
l2 = [int(l[i]) if i == 0 else l[i] for i in range(len(l))]
# print(l2)
count = 0
for i in range(l2[0]):
    if l2[1] != l2[2]:
        l2[2] = l2[2][1:] + l2[2][0]
        count += 1
print(count)