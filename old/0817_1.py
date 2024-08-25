n, k, t = map(int, input().split())

print("YES" if k * t % n == 0 else "NO")