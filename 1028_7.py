n, m = map(int, input().split())
l = list(map(int, input().split()))
l.remove(m)
for i in l:
    print(i)