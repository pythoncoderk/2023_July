n = int(input())
a = list(map(int, input().split()))
t, q = map(int, input().split())
l = [list(map(int, input().split())) for i in range(q)]
l2 = []
for i in range(q):
    l2.append(a[l[i][0]-1] * l[i][1])
# print(n)
# print(a)
# print(t, q)
# print(l)
for i in range(q):
    if t - l2[i] >= 0:
        t -= l2[i]
print(t)