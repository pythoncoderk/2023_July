n = int(input())
l = [list(map(int, input().split())) for i in range(5)]

for i in l:
    print(*i)
