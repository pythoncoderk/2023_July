n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
l.sort(reverse=True)

for i in l:
    print(*i)