v, t, s, d = map(int, input().split())

# print(v, t, s, d)

x = d / v

print("No" if t <= x <= s else "Yes")