h, w, a, b = map(int, input().split())
for i in range(h):
    for j in range(w):
        if j == w - 1:
            print(f"({a}, {b})")
            if i == h - 1:
                pass
            else:
                print("=" * (6 * w + 3 * (w - 1)))
        else:
            print(f"({a}, {b}) | ", end="")