a, b, c = map(int, input().split())

if c == 0:
    a -= 1
else:
    b -= 1

if c == 0:
    if a >= b:
        print("Takahashi")
    else:
        print("Aoki")
else:
    if a <= b:
        print("Aoki")
    else:
        print("Takahashi")
