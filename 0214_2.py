m = int(input())
l = [int(input()) for i in range(m)]
n = int(input())
l2 = [int(input()) for i in range(n)]

# print(m)
# print(l)
# print(n)
# print(l2)
bands = "A"
for i in range(1, 32):
    if i in l and i in l2:
        print(bands)
        if bands == "A":
            bands = "B"
        else:
            bands = "A"
    elif i in l:
        print("A")
    elif i in l2:
        print("B")
    else:
        print("x")