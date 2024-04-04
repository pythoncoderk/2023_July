n = int(input())
l = list(map(int, input().split()))
t, q = map(int, input().split())
l2 = [list(map(int, input().split())) for i in range(q)]

for i in range(q):
    l2[i][0] -= 1

# print(n)
# print(l)
# print(t, q)
# print(l2)

for i in range(q):
    if l[l2[i][0]] * l2[i][1] <= t:
        t -= l[l2[i][0]] * l2[i][1]
print(t)
