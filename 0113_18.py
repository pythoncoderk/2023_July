n = int(input())
l = list(map(int, input().split()))

print(l)


for i in range(n):
    min_l = l[i]
    for j in range(i, n):
        if l[j] < min_l:
            min_l = l[j]
    min_l, l[i] = l[i], min_l
    print(l)

