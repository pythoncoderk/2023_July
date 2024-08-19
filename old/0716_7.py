v, a, b, c = map(int, input().split())

# print(v, a, b, c)

now = "a"
while True:
    if now == "a":
        v -= a
        now = "b"
        if v < 0:
            print("F")
            break
    elif now == "b":
        v -= b
        now = "c"
        if v < 0:
            print("M")
            break
    elif now == "c":
        v -= c
        now = "a"
        if v < 0:
            print("T")
            break

