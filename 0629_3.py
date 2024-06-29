s, t, x = map(int, input().split())

x += 0.5

# print(x)

if s < t:
    print("Yes" if s <= x <= t else "No")
else:
    print("Yes" if s <= x or t >= x else "No")