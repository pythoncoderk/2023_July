n = int(input())
l = list(map(int, input().split()))

k = 0
g = 0
for i in l:
    if i % 2 == 0:
        g += 1
    else:
        k += 1

print(g, k)