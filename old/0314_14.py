m, n = map(int, input().split())

l = [int(input()) for i in range(m)]
l3 = []
for i in range(m):
    l2 = [l[i], n % l[i]]
    l3.append(l2)

# print(l3)
l4 = l3[::]
l4 = sorted(l4, key=lambda x: (x[1], -x[0]))

# print(l4)

for i in range(m):
    if l4[0] == l3[i]:
        print(i+1)
        break


