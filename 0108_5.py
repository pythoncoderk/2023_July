n, k = map(int, input().split())
l = list(map(int, input().split()))
l2 = []
for i in range(n - k + 1):
    l3 = []
    for j in range(k):
        l3.append(l[i+j])
    l2.append(sum(l3))
print(max(l2))