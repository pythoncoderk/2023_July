a, b = map(int, input().split())

for i in range(1, 10):
    count = 0
    for j in range(0, 10):
        x = (int(str(i) + str(j))) * j
        y = int(str(a) + str(i) + str(b))
        if x == y:
            print(i, j)
            exit()
print("No")