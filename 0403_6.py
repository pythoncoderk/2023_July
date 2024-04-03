l1 = list(input())
l2 = list(input())

print(l1)
print(l2)

l3 = [int(l1[i]) for i in range(len(l1)) if l1[i] != " "]
print(l3)

for i in range(len(l2)):
    x = ord(l2[i]) - 97
    if l3[x] > 0:
        print(l2[i], end="")
        l3[x] -= 1
