l = list(map(int, input()))
for i in range(len(l)):
    if i % 3 == 0 and i != 0:
        print(f",{l[i]}", end="")
    else:
        print(l[i], end="")

