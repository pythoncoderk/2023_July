x, y = map(int, input().split())
for i in range(10):
    if i == 9:
        print(x)
    else:
        print(x, end=" ")
        x += y