l2 = []

while True:
    l = list(map(int, input().split()))
    l = reversed(l)
    l2.insert(0, l)

    if len(l) == 1:
        break

# print(l2)

l3 = []
for i in range(len(l2)):
    l3 += l2[i]

# print(l3)

for i in range(len(l3)):
    if l3[i] == 1:
        print(i + 1)
        break

print(sum(l3))