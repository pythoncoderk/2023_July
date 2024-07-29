n, m = map(int, input().split())

for i in range(1, n + 1):
    if i == n:
        print(i)
    else:
        print(i, end=" ")

for i in range(1, m + 1):
    if i == m:
        print(i)
    else:
        print(i, end=" ")