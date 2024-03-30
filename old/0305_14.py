n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
l = sorted(l, key=lambda x: x[1], reverse=False)
for i in l:
    print(*i)