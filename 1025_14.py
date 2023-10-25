x, y = map(int, input().split())
if x > y:
    print(f"-{x - y}")
elif x == y:
    print(0)
else:
    print(f"+{y - x}")