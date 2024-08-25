n, k = map(int, input().split())
l = list(map(int, input().split()))
l2 = list(map(int, input().split()))

max_l = -99999999999999999999999999999999
for i in range(n):
    for j in range(k):
        max_l = max([max_l, l[i] * l2[j]])

print(max_l)