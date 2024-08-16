n, a, b = map(int, input().split())

x1 = n + a
x2 = n - a

if x1 + b == 0 or x1 - b == 0 or x2 + b == 0 or x2 - b == 0:
    print("YES")
else:
    print("NO")