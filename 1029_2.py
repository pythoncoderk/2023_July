n, m, k = map(int, input().split())
l = list(map(int, input().split()))
l.insert(m-1, k)
for i in l:
    print(i)