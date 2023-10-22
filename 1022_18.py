n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    l[i].pop(0)
    print(sum(l[i]))