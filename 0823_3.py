n = int(input())
l = list(map(int, input().split()))

for i in range(n):
    l2 = []
    for j in range(n):
        l2.append(l[i] * l[j])
    print(*l2)