n, q = map(int, input().split())

l = [i for i in range(1, n + 1)]

# print(l)

count = 0
for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            if l[i] + l[j] + l[k] == q:
                count += 1

print(count)
