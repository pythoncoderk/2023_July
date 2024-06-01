n = int(input())

l = [input() for i in range(n)]

# print(n)
# print(l)

for i in range(n):
    l2 = []
    for j in range(4):
        l2.append(l[i].count(l[i][j]))
    if max(l2) == 4:
        print("Four Card")
    elif max(l2) == 3:
        print("Three Card")
    elif l2.count(2) == 4:
        print("Two Pair")
    elif l2.count(2) == 2:
        print("One Pair")
    else:
        print("No Pair")
