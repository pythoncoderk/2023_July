l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
l2 = list(map(int, input().split()))
for i in range(3):
    for j in range(l2[i]):
        if j == l2[i]-1:
            print(l.pop(0))
        else:
            print(l.pop(0), end="")
