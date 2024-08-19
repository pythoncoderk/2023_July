n, t, a = map(int, input().split())

x = t + a

y = n - x

print("Yes" if (t + y > a and t > y + a and t > a) or (t + y < a and t < y + a and t < a) else "No")