n = int(input())
l = list(map(str, input().split()))
# print(l)

l2 = [int(l[i]) if l[i] != "x10" else "x10" for i in range(n)]
# print(l2)

max_l = 0
for i in range(n):
    if l2[i] != "x10":
        if max_l < l2[i]:
            max_l = l2[i]
x10 = False
for i in range(n):
    if l2[i] == "x10":
        l2[i] = 1
        x10 = True

if 0 in l2:
    for i in range(n):
        if l2[i] == max_l:
            l2[i] = 0
if x10:
    total = ((sum(l2)-1) * 10)
else:
    total = sum(l2)

print(total)