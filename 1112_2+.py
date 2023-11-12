n = int(input())
l = list(map(int, input().split()))
m = int(input())
if m in l:
    for i in range(n):
        if l[i] == m:
            print(l.index(m)+1)
            l[i] = 999
