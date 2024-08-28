n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

l = sorted(l, key=lambda x:(x[0], x[1]), reverse=True)
for i in range(n):
    print(*l[i])