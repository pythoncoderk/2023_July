l = list(map(int, input().split()))

x = l[0] * (l[1] / 100)
y = l[0] * (l[2] / 100)

print(int(y - x))
