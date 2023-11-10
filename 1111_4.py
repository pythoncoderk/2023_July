n = int(input())
l = [int(input()) for i in range(n)]
x, y = map(int, input().split())
a = l.index(x)
b = l.index(y)
l[a] = y
l[b] = x
for i in l:
    print(i)
