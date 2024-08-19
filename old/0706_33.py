n, k = map(int, input().split())
l = list(map(int, input().split()))

for i in range(n):
    for q in range(i + 1, n):
        for j in range(k):
            print(l[j])
