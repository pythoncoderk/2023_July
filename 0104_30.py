n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
k, t = map(int, input().split())
for i in range(n):
    l[i][1] = int(l[i][1])

l2 = [l[i][0] for i in range(n) if l[i][1] >= k and l[i][1] <= t]
for i in l2:
    print(i)
