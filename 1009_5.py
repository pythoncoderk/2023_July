n = int(input())
x = 1
for i in range(n):
    for j in range(x):
        if j+1 == x:
            print(j+1)
        else:
            print(j+1, end=" ")
    x += 1