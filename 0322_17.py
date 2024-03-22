import re

n = int(input())
g = input()
l = [input() for i in range(n)]

# print(n)
# print(g)
# print(l)

count = 0
for i in range(n):
    x = re.search(g, l[i])
    if x is not None:
        count += 1
        print(l[i])
if count == 0:
    print("None")