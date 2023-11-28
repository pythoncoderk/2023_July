import re

n = input()
m = int(input())
l = [input() for i in range(m)]
# print(n, m)
# print(l)
l2 = []
for i in l:
    if re.search(n, i) == None:
        l2.append(i)
if l2 == []:
    print("none")
else:
    for i in l2:
        print(i)

