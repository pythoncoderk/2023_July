n = int(input())
l = list(map(int, input().split()))
k = int(input())
l2 = []
for i in range(n):
    if l[i] == k:
        l2.append(i + 1)
for i in l2:
    print(i)