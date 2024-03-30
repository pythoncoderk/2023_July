a, b = map(int, input().split())
x = 0
while True:
    if a + b != x:
        print(x)
        exit()
    else:
        x += 1