x, y = map(int, input().split())
for i in range(x):
    if i+1 == x:
        print(i+1)
    else:
        print(i+1, end=" ")
for j in range(y):
    if j+1 == y:
        print(j+1)
    else:
        print(j+1, end=" ")