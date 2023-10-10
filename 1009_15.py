x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
for i in range(x):
    if i+1 == x:
        print(f"({y}, {z})")
    else:
        print(f"({y}, {z})", end=", ")