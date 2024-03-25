s = list(input())

while s:
    for i in range(10):
        if s:
            print(s.pop(0), end="")
        else:
            exit()
    print()
