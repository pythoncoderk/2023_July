l = [5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
k = 22

l2 = [i for i in range((len(l) ** 2)-1)]

# print(l2)

count = 0
for i in range(len(l2)):
    total = 0
    x = bin(l2[i])
    x = list(x[2:])
    x = [int(x[ii]) for ii in range(len(x))]
    for j in range(len(x)):
        if x[j] == 1:
            total += l[j]
    if total == k:
        count += 1

print(count)