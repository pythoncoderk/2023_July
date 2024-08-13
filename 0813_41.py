n, m = map(int, input().split())
l = list(map(int, input().split()))

for i in range(n):
    if i + 1 == m:
        l.pop(i)
        break

for i in l:
    print(i)