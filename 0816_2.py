n, k = map(int, input().split())
l = [int(input()) for i in range(n)]

l2 = []
for i in l:
    if i >= k:
        l2.append(i)

for i in l2:
    print(i)