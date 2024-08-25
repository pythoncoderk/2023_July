n = int(input())

l = []
for i in range(n):
    x = input().split()
    if x[0] == "in":
        l.append(x[1])
    elif x[0] == "out":
        if len(l) > 0:
            l.pop(0)

if len(l) > 0:
    for i in l:
        print(i)
