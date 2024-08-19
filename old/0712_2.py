n, a, x, y = map(int, input().split())

# print(n, a, x, y)

if n < a:
    print(n * x)
    exit()

i = a * x
j = (n - a) * y

print(i + j)