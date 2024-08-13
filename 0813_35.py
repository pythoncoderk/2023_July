a, b, n = map(int, input().split())
l = list(map(int, input().split()))

for i in range(n):
    if a - 1 <= i <= b - 1:
        print(l[i])