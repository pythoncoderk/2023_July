import re

n = input()
m = int(input())
l = [input() for i in range(m)]
# print(n)
# print(m)
# print(l)
l2 = []
for i in range(m):
    x = re.search(n, l[i])
    if x == None:
        l2.append(l[i])
if l2 == []:
    print("none")
else:
    for i in l2:
        print(i)