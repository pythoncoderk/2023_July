l = list(input())
l2 = [int(l[i]) for i in range(len(l))]

total = 0
for i in l2:
    total += i

print(total)