n = int(input())
l = list(map(int, input().split()))
l.sort()
# print(n)
# print(l)

l2 = []
l3 = []
while l:
    if l2 == []:
        x = l.pop(0)
        l2.append(x)
    else:
        x = l.pop(0)
        if l2[-1] + 1 == x:
            l2.append(x)
        else:
            l3.append(l2)
            l2 = []
            l2.append(x)
if l2:
    l3.append(l2)

# print(l3)

total = 0
for i in range(len(l3)):
    total += max(l3[i])
print(total)