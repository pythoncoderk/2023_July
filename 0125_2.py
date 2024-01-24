import math
import sys

l = list(map(int, input().split()))
# print(l)
out_l = math.ceil(l[0] / l[1])
if out_l < l[2]:
    print("none")
    sys.exit()
x = 0
l2 = []
while l[0] != 0:
    l3 = []
    for i in range(1+x, l[1]+1+x):
        if l[0] > 0:
            l3.append(i)
            l[0] -= 1
        else:
            break
    l2.append(l3)
    x += l[1]
print(*l2[l[2]-1])