n = int(input())
l = list(map(int, input().split()))
m = int(input())

if m in l:
    l.reverse()
    x = l.index(m)
    print(n - x)
else:
    print(0)