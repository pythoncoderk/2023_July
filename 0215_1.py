n = int(input())
l = list(map(int, input().split()))
l2 = l[::]
# print(n)
# print(l)

max_l = max(l2)
for i in range(n):
    if max_l == l2[i]:
        l2[i] = -100
# print(l2)

count_g = l2.count(-100)
# print(count_g)
max_s = max(l2)
if count_g == 1:
    for i in range(n):
        if max_s == l2[i]:
            l2[i] = -200
# print(l2)
count_s = l2.count(-200)
max_b = max(l2)
if count_s == 1:
    for i in range(n):
        if max_b == l2[i]:
            l2[i] = -300
# print(l2)

for i in range(n):
    if l2[i] == -100:
        l2[i] = "G"
    elif l2[i] == -200:
        l2[i] = "S"
    elif l2[i] == -300:
        l2[i] = "B"
    else:
        l2[i] = "N"
# print(l2)

for i in l2:
    print(i)

