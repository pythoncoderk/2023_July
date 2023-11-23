n, k = map(int, input().split())
l = [int(input()) for i in range(n)]
# print(n, k)
# print(l)
l2 = []
for i in range(n):
    l2.append(abs(l[i] - k))
# print(l2)
min_time = min(l2)
# print(min_time)
l3 = []
for i in range(n):
    if min_time == l2[i]:
        l3.append(l[i])
# print(l3)
l3.sort()
for i in l3:
    print(i)