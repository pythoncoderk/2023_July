import re

n = int(input())
s1 = input()
l = [input() for i in range(n)]

count = 0
for i in range(n):
    x = re.search(s1, l[i])
    if x is not None:
        print(l[i])
        count += 1

if count == 0:
    print("None")