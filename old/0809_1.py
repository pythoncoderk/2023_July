s = input()
chk = True

if "." not in s:
    chk = False

if "." not in s:
    while True:
        if s[0] == "0":
            s = s[1:]
        else:
            break
else:
    x = s.index(".")
    x1 = s[:x + 1]
    x2 = s[x + 1:]
    while True:
        if x1[0] == "0" and x1[1] != ".":
            x1 = x1[1:]
        else:
            break

        while True:
            if x2[-1] == "0":
                x2 = x2[:-1]
            else:
                break
    x3 = ""
    for i in x2:
        if i != ".":
            x3 += i


if chk:
    print(x1 + x3)
else:
    print(s)