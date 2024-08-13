n, m = map(int, input().split())
l = list(map(int, input().split()))

for i in range(m):
    if l[i] == n:
        print(i + 1)
        break