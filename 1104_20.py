n = int(input())
x, y, z = map(int, input().split())
if n >= x:
    print(n * y)
else:
    print(n * z)