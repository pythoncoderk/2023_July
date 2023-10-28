x, y = map(int, input().split())
l = list(map(int, input().split()))
l.pop(y-1)
for i in l:
    print(i)