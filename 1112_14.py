n = int(input())
l = list(map(int, input().split()))
m = int(input())

if m in l:
    print(l.index(m)+1)
else:
    print(0)