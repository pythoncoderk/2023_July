x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(x)]
l_f = []
for i in range(x):
    l_f.append(max(l[i]))
print(max(l_f))
