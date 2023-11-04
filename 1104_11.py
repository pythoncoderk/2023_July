n = list(input())
l = []
for i in range(len(n)):
    if n[i] == "a" or n[i] == "e" or n[i] == "i" or n[i] == "o" or n[i] == "u":
        pass
    else:
        l.append(n[i])
for i in range(len(l)):
    if i == len(l)-1:
        print(l[i])
    else:
        print(l[i], end="")