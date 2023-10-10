a, b, c, d = map(int, input().split())
for i in range(a):
    for j in range(b):
        if j+1 == b:
            print(f"({c}, {d})")
            if i+1 == a:
                pass
            else:
                print("=" * ((int(b) * 9) - 3))
        else:
            print(f"({c}, {d})", end=" | ")