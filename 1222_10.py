x, y = map(int, input().split())
if x == y:
    print("eq")
elif x > y:
    print(f"{x}")
else:
    print(f"{y}")