x, y = map(int, input().split())
l = [int(input()) for i in range(x)]
for i in l:
    if i >= y:
        print(i)