n, m = map(int, input().split())
s = list(input())

for i in range(n):
    s[i] = int(s[i])

# print(n, m)
# print(s)

l3 = []
while s:
    l2 = []
    for i in range(m):
        if s == []:
            l2.append(0)
        else:
            l2.append(s.pop(0))
    l3.append(l2)
# print(l3)

x_l = l3.pop(0)
l4 = []
for i in range(len(l3)):
    l5 = []
    for j in range(m):
        l5.append(x_l[j] ^ l3[i][j])
    x_l = l5

for i in x_l:
    print(i, end="")