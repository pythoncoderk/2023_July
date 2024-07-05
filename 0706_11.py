a, b, c, d = map(int, input().split())

x = b / a
y = d / c

if x == y:
    print("DRAW")
    exit()

print("TAKAHASHI" if x > y else "AOKI")