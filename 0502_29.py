a, b = map(str, input().split())

# print(a, b)

for i in range(1, 10):
    for j in range(1, 10):
        x = int(str(i) + str(j)) * j
        y = int(a + str(i) + b)
        if x == y:
            print(i, j)
            exit()
print("No")