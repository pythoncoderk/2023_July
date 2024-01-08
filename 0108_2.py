n, k = map(int, input().split())
l = list(map(int, input().split()))
l3 = []
for i in range(n - k + 1):
    l2 = []
    for j in range(k):
        l2.append(l[i+j])
    l3.append(sum(l2))
print(max(l3))

