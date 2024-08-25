x, y, z = map(int, input().split())

print("YES" if z >= 10 or (x >= 10 and y >= 10) else "NO")