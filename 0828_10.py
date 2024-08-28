n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
l = sorted(l, key=lambda x:(x[1], x[0]), reverse=True)

for i in l:
    print(*i)