x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(x)]
for i in range(x):
    print(sum(l[i]))