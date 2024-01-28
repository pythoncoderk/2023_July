n = int(input())
l = list(map(int, input().split()))
print(l)
xxx = 0
l2 = l[::]
total = []
for i in range(n):
    x = []
    for j in range(n):
        x.append(l2[j])
    x[i] = x[i]+1

