import sys

n = 57

for i in range(2, 57):
    if n % i == 0:
        print("NO")
        sys.exit()
    else:
        pass
print("YES")