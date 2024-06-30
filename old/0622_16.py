a, b, c, k = map(int, input().split())
s, t = map(int, input().split())

all_prason = s + t

if all_prason >= k:
    print((a - c) * s + (b - c) * t)
else:
    print(s * a + b * t)