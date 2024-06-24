n = int(input())
l = list(map(int, input().split()))
m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]

# print(n)
# print(l)
# print(m)
# print(l2)

l3 = []
x = 0
for i in range(n):
    x += l[i]
    l3.append(x)
l3.insert(0, 0)

# print(l3)

l4 = []
x = 0
for i in range(n):
    if l[i] == 0:
        x += 1
        l4.append(x)
    else:
        l4.append(x)

l4.insert(0, 0)

# print(l4)

for i in range(m):
    win = l3[l2[i][1]] - l3[l2[i][0] - 1]
    lose = l4[l2[i][1]] - l4[l2[i][0] - 1]
    if win == lose:
        print("draw")
    elif win > lose:
        print("win")
    else:
        print("lose")