n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

l2 = []
for i in range(n):
    s = ""
    for j in range(len(l[i])):
        if l[i][j].isdecimal():
            s += l[i][j]
    l2.append(s)
# print(l2)

l3 = [int(l2[i]) for i in range(len(l2))]

# print(l3)

l4 = [[l3[i], l[i]] for i in range(n)]

# print(l4)

x_sort = sorted(l4, key=lambda x: x[0])
# print(x_sort)

for i in range(n):
    print(x_sort[i][1])