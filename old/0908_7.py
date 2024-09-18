y, x, n = map(int, input().split())
for _ in range(n):
    inp = input()
    if inp == "N":
        y -= 1
        print(y, x)
    elif inp == "S":
        y += 1
        print(y, x)
    elif inp == "W":
        x -= 1
        print(y, x)
    else:
        x += 1
        print(y, x)
