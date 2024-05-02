n = int(input())
l = list(map(int, input().split()))
t, q = map(int, input().split())
l2 = [list(map(int, input().split())) for i in range(q)]

# print(n)
# print(l)
# print(t, q)
# print(l2)


for i in range(q):
    if t - l[l2[i][0]-1] * l2[i][1] >= 0:
        t -= l[l2[i][0]-1] * l2[i][1]

print(t)