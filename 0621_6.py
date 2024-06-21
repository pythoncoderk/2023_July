n, m = map(int, input().split())

x = n - m
y = n - x - 1

print(x if x < y else y)