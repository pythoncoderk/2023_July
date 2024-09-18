a, b, c, d = map(int, input().split())

t = b / a
ao = d / c

if t == ao:
    print("DRAW")
    exit()

print("TAKAHASHI" if t > ao else "AOKI")