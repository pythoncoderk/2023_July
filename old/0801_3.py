h, w, a, b = map(int, input().split())

for i in range(h):
    for j in range(w):
        print("({}, {})".format(a, b), end="")
        if j == w - 1:
            print()
        else:
            print(end=" | ")
    if i != h - 1:
        print("=" * ((6 * w) + ((w - 1) * 3)))