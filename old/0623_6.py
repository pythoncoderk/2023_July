l = [int(input()) for i in range(3)]
l2 = l[::-1]
l2.sort(reverse=True)

# print(l)
# print(l2)

l4 = []
for i in range(3):
    l4.append(l2.index(l[i]) + 1)

# print(l4)


for i in range(3):
    print(l4[i])
