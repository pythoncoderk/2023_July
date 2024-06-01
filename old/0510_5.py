n = int(input())
l = list(map(int, input().split()))
q = int(input())
l2 = [list(map(int, input().split())) for i in range(q)]

# print(n)
# print(l)
# print(q)
# print(l2)

x = 0
for i in range(n):
    l[i] += x
    x = l[i]

l.insert(0, 0)

for i in range(len(l2)):
    l2[i][0] -= 1

# print(l)
# print(l2)

for i in range(len(l2)):
    count = l2[i][1] - l2[i][0]
    win = l[l2[i][1]] - l[l2[i][0]]
    lose = count - win
    if win == lose:
        print("draw")
    elif win > lose:
        print("win")
    else:
        print("lose")