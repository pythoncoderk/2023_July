k = int(input())

l = [i for i in range(1, k + 1)]

# print(l)

count = 0
for i in range(k):
    for j in range(k):
        if l[i] % 2 != 0 and l[j] % 2 == 0:
            count += 1

print(count)