n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(m)]
print(l)

s_l = [0 for i in range(n)]
print(s_l)

for i in range(m):
    if sum(s_l[l[i][1]-1:l[i][0]+1]) == 0:
        for j in range(l[i][1]-1, l[i][0]+1):
            s_l[j] = 1
print(s_l)