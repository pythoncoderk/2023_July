l = list(map(int, input().split()))

# print(l)

x = l[0] - (l[0] * (l[1] / 100))
y = x - (x * (l[2] / 100))
print(y)