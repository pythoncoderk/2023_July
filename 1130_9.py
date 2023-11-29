n = int(input())

l = [i for i in range(1, 10)]
l2 = [i * n for i in l]
for i in range(9):
    if i == 8:
        print(l2[i])
    else:
        print(l2[i], end=" ")