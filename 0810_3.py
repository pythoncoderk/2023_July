l = list(map(int, input().split()))
l2 = [int(input()) for i in range(l[0])]

# print(l)
# print(l2)

count = 0
now = l2[0]
if l[1] <= now <= l[2]:
    count += 1
for i in range(1, l[0]):
    now += l2[i]
    if l[1] <= now <= l[2]:
        count += 1

print(count)