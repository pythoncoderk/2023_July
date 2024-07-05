a, b, c, k = map(int, input().split())
s, t = map(int, input().split())

# print(a, b, c, k)
# print(s, t)

kids = a * s
adult = b * t

price_down = 0
if s + t >= k:
    price_down = (s + t) * c

print(kids + adult - price_down)