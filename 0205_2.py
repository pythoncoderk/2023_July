n, x = map(int, input().split())
l = [int(input()) for i in range(n)]

print(n, x)
print(l)
two = []
while x != 0:
    y = int(x % 2)
    x //= 2

    two.append(y)
    print(x)
    print(y)