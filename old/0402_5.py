N = int(input())
l = list(map(int, input().split()))

for i in range(1, n):
    count = 0
    for j in range(n):
        if i == l[j]:
            count += 1
    print(count)