n, k = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, k)
# print(l)

l.sort()
l2 = [abs(l[i]-k) for i in range(n)]
# print(l)
# print(l2)
min_l = min(l2)

for i in range(n):
    if min_l == l2[i]:
        print(l[i])