n = list(input())
n = [int(n[i]) for i in range(len(n))]
n.reverse()

l = []
for i in range(len(n)):
    if i == 0:
        l.append(1)
    elif i == 1:
        l.append(2)
    else:
        l.append(l[i-1] * 2)
# print(l)

total = 0
for i in range(len(n)):
    total += l[i] * n[i]

print(total)