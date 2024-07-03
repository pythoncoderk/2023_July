n = int(input())
l = list(map(str, input().split()))

# print(n)
# print(l)

zero = 0
ten = 0
for i in range(n):
    if l[i] != "0" and l[i] != "x10":
        l[i] = int(l[i])
    elif l[i] == "0":
        l[i] = 0
    elif l[i] == "x10":
        l[i] = 10000

# print(l)

l2 = []
while l:
    if l[0] == 0:
        zero += 1
        l.pop(0)
    else:
        x = l.pop(0)
        l2.append(x)

# print(l2)

l3 = []
while l2:
    if l2[0] == 10000:
        l2.pop(0)
        ten += 1
    else:
        x = l2.pop(0)
        l3.append(x)

# print(l3)

max_l = max(l3)
if zero >= 1:
    for i in range(len(l3)):
        if l3[i] == max_l:
            l3[i] = 0

if ten >= 1:
    print(sum(l3) * 10)
else:
    print(sum(l3))


