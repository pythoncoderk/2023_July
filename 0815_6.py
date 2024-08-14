n = int(input())
a = []
for i in range(n):
    x = input().split()
    if x[0] == "out" and len(a) != 0:
        a.pop(0)
    elif x[0] == "in":
        a.append(x[1])
for i in a:
    print(i)
