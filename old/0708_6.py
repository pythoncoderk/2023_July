n = list(input())

for i in range(len(n)):
    if n[i] == "9":
        n[i] = "1"
    else:
        n[i] = "9"

for i in range(len(n)):
    print(n[i], end="")