n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

l2 = l[::]
x = l2.pop(0)
l3 = []
count = []
while l2:
    if x + 1 == l2[0]:
        count.append(x)
        x = l2.pop(0)
    else:
        count.append(x)
        l3.append(count)
        x = l2.pop(0)
        count = []
# print(l3)

l4 = []
for i in range(len(l3)):
    l4.append(len(l3[i]))
# print(l4)

if l4 == []:
    print(l[0], l[0])
    exit()
max_l = max(l4)

final_l = 0
for i in range(len(l4)):
    if l4[i] == max_l:
        final_l = i
        break

print(f"{l3[final_l][0]} {l3[final_l][-1]}")

