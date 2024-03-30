l = list(map(int, input().split()))
ab = "a"
for i in range(len(l)):
    if ab == "a":
        print("A" * l[i], end="")
        ab = "b"
    elif ab == "b":
        print("B" * l[i], end="")
        ab = "a"
