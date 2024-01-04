import math

n = int(input())
l = []
for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
        l.append(i)
if len(l) != 0:
    print("YES")
else:
    print("NO")