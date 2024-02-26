n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
d = {l[k][0]: int(l[k][1]) for k in range(n)}

d_sort = sorted(d.items(), key=lambda x:x[1], reverse=True)

print(d_sort[1][0])