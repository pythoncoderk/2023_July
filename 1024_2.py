import sys
n = int(input())
for a in range(1, n):
    for b in range(1, n):
        c = n - a + b
        if (a ** 2) == (b ** 2) + (c ** 2):
            print("YES")
            sys.exit()
        else:
            pass
print("NO")