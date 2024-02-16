import math

n, m = map(int, input().split())
s = list(input())

# print(n, m)
# print(s)

l = []
l2 = []
for i in range(math.ceil(n/m)):
    for j in range(m):
        if s:
            x = s.pop(0)
            l2.append(x)
        else:
            l2.append("0")
    l.append(l2)
    l2 = []
for i in range(math.ceil(n/m)):
    for j in range(m):
        l[i][j] = int(l[i][j])
# print(l)
final_l = l.pop(0)
while l:
    x = l.pop(0)
    for i in range(m):
        final_l[i] = final_l[i] ^ x[i]

for i in final_l:
    print(i, end="")