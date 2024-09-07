h, w = map(int, input().split())

x = 0
for i in range(h):
    l = list(input())

    for j in range(len(l)):
        if j == 0:
            if l[j + 1] == "#":
                print(x, j)
        elif j == len(l) - 1:
            if l[j - 1] == "#":
                print(x, j)
        else:
            if l[j - 1] == "#" and l[j + 1] == "#":
                print(x, j)

    x += 1

