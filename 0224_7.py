import re

n = int(input())
s = input()
q = int(input())
l = [list(map(str, input().split())) for i in range(q)]
# print(n)
# print(s)
# print(q)
# print(l)
l2 = []
for i in range(len(l)):
    if l[i][0] != l[i][1]:
        l2.append(l[i])

for i in range(len(l2)):
    s = re.sub(l2[i][0], l2[i][1], s)
print(s)