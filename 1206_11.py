n = int(input())
l = list(map(int, input().split()))
m = int(input())
if m in l:
    l.reverse()
    # print(l)
    x = l.index(m)
    print(len(l) - x)
else:
    print(0)