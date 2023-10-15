n, a, b = map(int, input().split())
n1 = n + a
n2 = n - a
if (n1 + b == 0 or n1 - b == 0) or (n2 + b == 0 or n2 - b == 0):
    print("YES")
else:
    print("NO")