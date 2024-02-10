h, w, x = map(int, input().split())
l = [input() for i in range(h)]

# print(h, w, x)
# print(l)
l2 = "".join(l)
l2 = list(l2)
# print(l2)

while l2:
    for i in range(x):
        if not l2:
            break
        else:
            p = l2.pop(0)
            print(p, end="")
    print()