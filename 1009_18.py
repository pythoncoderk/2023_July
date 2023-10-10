a, b, c, d = input().split()
a = int(a)
b = int(b)
c = c.rjust(9, " ")
d = d.rjust(9, " ")

for i in range(a):
    for j in range(b):
        if j+1 == b:
            print(f"({c}, {d})")
            if i+1 == a:
                pass
            else:
                print("=" * ((25 * b)-3))
        else:
            print(f"({c}, {d})", end=" | ")

