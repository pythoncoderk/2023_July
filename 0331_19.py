n = list(map(int, input().split()))
l = [int(input()) for i in range(n[0])]

# print(n)
# print(l)

total = 0
count = 0
for i in range(n[0]+1):
    if i == n[0]:
        total += l[i-1] * count
    elif l[i] <= n[1]:
        count += 1
        total -= l[i]
    elif l[i] >= n[2]:
        total += l[i] * count
        count = 0
print(total)