n = list(input())
for i in range(len(n)):
    if i % 9 == 0 and i != 0:
        print(n[i])
    else:
        print(n[i], end="")