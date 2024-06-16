r, g, b = map(str, input().split())

x = r + g + b
x = int(x)

print("YES" if x % 4 == 0 else "NO")