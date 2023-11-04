l = list(input())
for i in range(len(l)):
    if i == len(l)-1:
        if l[i] == "0":
            print("C")
        elif l[i] == "1":
            print("A")
        else:
            print("B")
    else:
        if l[i] == "0":
            print("C", end="")
        elif l[i] == "1":
            print("A", end="")
        else:
            print("B", end="")

