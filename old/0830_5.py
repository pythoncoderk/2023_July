n = int(input())
ab = [None] * n

for i in range(n):
    [a, b] = input().split()
    a = int(a)
    b = int(b)
    ab[i] = [a, b]

ab.sort(reverse=True)

for i in range(n):
    [a, b] = ab[i]
    print(a, b)