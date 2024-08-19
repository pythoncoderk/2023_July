h, w, a, b = map(int, input().split())
for i in range(h):
    for j in range(w):
        print("({:>9}, {:>9})".format(a, b), end="")
        if j != w - 1:
            print(end=" | ")
        else:
            print()
    if i != h - 1:
        print("=" * (22 * w + 3 * (w - 1)))