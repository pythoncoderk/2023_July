t = int(input())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(t)
# print(n)
# print(l)

l2 = [0 for i in range(t + 1)]

# print(l2)

for i in range(n):
    l2[l[i][0]] += 1
    l2[l[i][1]] -= 1

# print(l2)

l3 = []
x = 0
for i in range(len(l2)):
    x += l2[i]
    l3.append(x)

# print(l3)

for i in range(len(l3)-1):
    print(l3[i])