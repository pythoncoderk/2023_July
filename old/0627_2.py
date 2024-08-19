n, m = map(int, input().split())
x = int(input())
y = n
while n <= 1500:
    print(n, abs(x - n))
    n += y
