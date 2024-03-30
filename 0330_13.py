h, w, x = map(int, input().split())
l = [input() for i in range(h)]

# print(h, w, x)
# print(l)

marge = ""
for i in range(h):
    marge += l[i]

# print(marge)

xxx = 0
while marge:
    if xxx == x:
        print()
        xxx = 0
    else:
        print(marge[0], end="")
        marge = marge[1:]
        xxx += 1