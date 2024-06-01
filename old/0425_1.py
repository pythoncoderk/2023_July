l = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))
l4 = list(map(int, input().split()))

# print(l)
# print(l2)
# print(l3)
# print(l4)

x = 0
y = 0
if l3[l[0]-1] > l3[l[1]-1]:
    x = l[1]
else:
    x = l[0]

if l3[l2[0]-1] > l3[l2[1]-1]:
    y = l2[1]
else:
    y = l2[0]

l5 = [x, y]
l5.sort()

if l4[0] < l4[1]:
    print(l5[0])
    print(l5[1])
else:
    print(l5[1])
    print(l5[0])

