n, a, b, mod = map(int, input().split())
l = [int(input()) for i in range(n)]
for i in range(n):
    print((a * l[i] + b) % mod)