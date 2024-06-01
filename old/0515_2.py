import math

n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

for i in range(n):
    x = int(math.sqrt(l[i]))
    chk = True
    for j in range(2, x+1):
        if l[i] % j == 0:
            chk = False
            break
    if chk:
        print("Yes")
    else:
        print("No")
