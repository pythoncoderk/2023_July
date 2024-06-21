n, m = map(int, input().split())

x = n - m
y = m - 1

print(y if x > y else x)