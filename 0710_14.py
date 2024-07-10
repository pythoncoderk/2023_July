n = int(input())
l = list(map(int, input().split()))

l2 = []
for i in range(n - 1):
    if l[i] == 2 and l[i + 1] == 0:
        l2.append(i + 1)

if len(l2) == 0:
    print(-1)
else:
    print(*l2)