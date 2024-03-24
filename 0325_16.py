t, u = map(int, input().split())

if t < 0:
    print(abs(u) - abs(t))
elif t > 0 and u > 0:
    print(t - u)
else:
    print(t + abs(u))