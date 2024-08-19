h, w = map(int, input().split())
a, b = map(int, input().split())

x = h * w - (a * w + b * h - a * b)
print(x)
