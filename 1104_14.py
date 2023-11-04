n = list(input())
n.pop(int(input())-1)
for i in range(len(n)):
    if i == len(n)-1:
        print(n[i])
    else:
        print(n[i], end="")