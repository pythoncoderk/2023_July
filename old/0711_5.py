l, r, d = map(int, input().split())

l2 = [i for i in range(l, r + 1)]

count = 0
for i in range(len(l2)):
    if l2[i] % d == 0:
        count += 1

print(count)