n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
k, iii = map(int, input().split())

for i in range(n):
    l[i][1] = int(l[i][1])

for i in range(n):
    if k <= l[i][1] <= iii:
        print(l[i][0])