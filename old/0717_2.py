a, b, c, d, e, f, x = map(int, input().split())

# print(a, b, c, d, e, f, x)

def chk(a, b, c, x):
    run = 0
    while x > 0:
        if x - a >= 0:
            x -= a
            run += a
            x -= c
        else:
            run += x
            break
    return run * b


taka = chk(a, b, c, x)
aoki = chk(d, e, f, x)

if taka == aoki:
    print("Draw")
elif taka > aoki:
    print("Takahashi")
else:
    print("Aoki")