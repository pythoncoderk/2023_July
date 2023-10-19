n = list(input())
n = list(set(n))
n.sort()
if n[0] == 0:
    n = str(n[1:]) + "0"

for i in n:
    print(i, end="")