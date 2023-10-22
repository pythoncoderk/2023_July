n = int(input())
x = 1
for i in range(n):
    for j in range(x):
        if j == x-1:
            print(j+1)
            x += 1
        else:
            print(j+1, end=" ")