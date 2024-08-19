n, m = map(int, input().split())
l = [int(input()) for i in range(m)]

for i in range(m):
    print("Yes" if l[i] % n == 0 else "No")