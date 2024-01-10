n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

l2 = []
l3 = []
for i in range(n-1):
    if l[0]+1 == l[1]:
        l2.append(l.pop(0))
    else:
        l2.append(l.pop(0))
        l3.append(l2)
        l2 = []
l4 = [len(i) for i in l3]
# print(l4)
x = l4.index(max(l4))
print(f"{l3[x][0]} {l3[x][-1]}")