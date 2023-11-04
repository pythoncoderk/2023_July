n, m = map(int, input().split(":"))
if n - 8 < 0:
    print(f"{24 + (n - 8)}:{m}")
else:
    print(f"{n - 8}:{m}")