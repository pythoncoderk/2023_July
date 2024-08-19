n = int(input())

d = {}
for i in range(n):
    x = input()
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1

d2 = sorted(d.items(), key=lambda x: x[0])
l = list(d2)

for i in range(len(l)):
    print(l[i][0], l[i][1])