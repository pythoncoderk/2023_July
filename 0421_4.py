import re

n = input()
m = int(input())
l = [input() for i in range(m)]

# print(n)
# print(m)
# print(l)
count = 0
for i in range(m):
    x = re.search(n, l[i])
    if x is None:
        print(l[i])
        count += 1
if count == 0:
    print("none")

