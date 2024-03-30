n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = input()

for i in range(n):
    if l[i][1] == m:
        print(l[i][0])