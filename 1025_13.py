n = int(input())
for i in range(10):
    if n > 9:
        n = 0
        print(n)
        n += 1
    else:
        print(n)
        n += 1