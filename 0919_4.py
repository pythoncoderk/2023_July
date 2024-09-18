n, m = map(int, input().split())

for i in range(m):
    x = int(input())
    print("Yes" if x % n == 0 else "No")