l = list(map(int, input().split()))
for i in range(l[0]):
    print("A", end="")

for i in range(l[1]):
    print("B", end="")

for i in range(l[2]):
    if i == l[2]-1:
        print("A")
    else:
        print("A", end="")