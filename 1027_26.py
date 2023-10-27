x, y, z = map(int, input().split())
l = list(map(int, input().split()))
for i in l:
    if i == x:
        print(y)
    elif i == y:
        print(x)
    else:
        print(i)