x = list(input())

while True:
    if x[-1] == "0" and len(x) != 1:
        x.pop()
    elif x[-1] == ".":
        x.pop()
        break
    elif len(x) == 1:
        break
    else:
        break

print("".join(x))
