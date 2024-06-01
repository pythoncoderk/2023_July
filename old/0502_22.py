n = int(input())
l = [int(input()) for i in range(n)]
m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]
l3 = [[l2[i][0]-1, l2[i][1]-1, l2[i][2]] for i in range(m)]

# print(n)
# print(l)
# print(m)
# print(l2)
# print(l3)

for i in range(m):
    x = 0
    if l[l3[i][0]] >= l3[i][2]:
        l[l3[i][0]] -= l3[i][2]
        x = l3[i][2]
        l[l3[i][1]] += x
    else:
        x = l[l3[i][0]]
        l[l3[i][0]] = 0
        l[l3[i][1]] += x

for i in l:
    print(i)
