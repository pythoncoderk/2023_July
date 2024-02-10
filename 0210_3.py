n = int(input())
l = [input() for i in range(n)]
# print(n)
# print(l)

for i in range(n):
    l2 = []
    for j in range(4):
        l2.append(l[i].count(l[i][j]))
    if 4 in l2:
        print("Four Card")
    elif 3 in l2:
        print("Three Card")
    elif l2.count(2) == 4:
        print("Two Pair")
    elif 2 in l2:
        print("One Pair")
    else:
        print("No Pair")