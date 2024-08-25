n, k = map(int, input().split())

l = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    print(sum(l[i]))

