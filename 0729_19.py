n = input()
x = len(n) % 3

for i in range(len(n)):
    if (i - x) % 3 == 0 and i != 0:
        print(",", end="")
    print(n[i], end="")
print()