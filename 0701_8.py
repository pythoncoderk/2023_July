n = int(input())
l = list(map(str, input().split()))
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]
for i in range(len(l2)):
    l2[i][1] = int(l2[i][1])

# print(n)
# print(l)
# print(m)
# print(l2)

d = {l[k]: 0 for k in range(n)}

# print(d)

for i in range(len(l2)):
    d[l2[i][0]] += l2[i][1]

# print(d)

x = list(d.items())
x = sorted(x, key=lambda x:(x[1]), reverse=True)

# print(x)

for i in range(len(x)):
    print(x[i][0])