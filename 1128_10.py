n = input()
for i in range(len(n)):
    if i == len(n)-1:
        if i % 2 == 0:
            print(n[i])
    else:
        if i % 2 == 0:
            print(n[i], end="")
