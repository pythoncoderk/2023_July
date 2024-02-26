n = int(input())
l = list(map(int, input().split()))

print(n)
print(l)

for i in range(n):
    for j in range(i-1, 0, -1):
        tmp = l[i]
        if l[j] > l[i]:
            l[j+1] = l[j]
            l[j] = tmp
