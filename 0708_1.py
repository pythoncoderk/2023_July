n = input()
for i in range(len(n)):
    if i % 3 == 0 and i != 0:
        print(',' + n[i], end="")
    else:
        print(n[i], end="")