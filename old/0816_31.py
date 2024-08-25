n = int(input())

l = list(map(int, input().split()))

total = 0
for i in range(n):
    if l[i] % 2 == 0:
        total += l[i]
    else:
        break

print(total)