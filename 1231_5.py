l = list(map(str, input().split()))
n = int(input())
l2 = [list(map(str, input().split())) for i in range(n)]

# print(l)
# print(n)
# print(l2)

l3 = []
for i in range(n):
    x = 0
    for j in range(6):
        if l2[i][j] in l:
            x += 1
    l3.append(x)

for i in l3:
    print(i)
