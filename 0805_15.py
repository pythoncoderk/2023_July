a, b = map(int, input().split())

n = 10000
n //= a
n %= b

print(n)