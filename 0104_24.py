n = int(input())
l = list(map(int, input().split()))
l2 = []
for i in range(n):
    if l[i] % 2 == 1:
        l2.append(i + 1)

print(max(l2))