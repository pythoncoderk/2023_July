n = list(input())
if "." in n:
    x = n.index(".")
    m = []
    for i in n:
        if i == ".":
            pass
        else:
            m.append(i)
    n = m
    n.insert(x, ".")

    for i in range(n.index(".")-1):
        if n[0] == "0":
            n.pop(0)
        else:
            break
    while n[-1] != ".":
        if n[-1] == "0":
            n.pop(-1)
        else:
            break
else:
    for i in range(len(n)):
        if n[0] == "0":
            n.pop(0)
        else:
            break
for i in n:
    print(i, end="")