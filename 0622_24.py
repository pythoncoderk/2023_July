l = [int(input()) for i in range(3)]
l3 = l[::-1]
l3.sort(reverse=True)

l2 = []
for i in range(3):
    for j in range(3):
        if l3[i] == l[j]:
            l2.append(j + 1)

# print(l2)

for i in l2:
    print(i)