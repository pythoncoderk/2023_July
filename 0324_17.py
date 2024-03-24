l = list(map(int, input().split()))

x = 65
for i in range(3):
    for j in range(l[i]):
        print(chr(x), end="")
        x += 1
    print()