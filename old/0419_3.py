n = int(input())
l = [int(input()) for i in range(n)]
m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]
# print(l2)
for i in range(m):
    l2[i][0] -= 1
    l2[i][1] -= 1

# print(n)
# print(l)
# print(m)
# print(l2)

l3 = l[:]
# print(l3)
count = 0
for i in range(m):
    l3[l2[i][0]] -= 1
    l3[l2[i][1]] -= 1
    chk = True
    for j in range(n):
        if l3[j] < 0:
            chk = False
    if chk:
        l = l3[:]
        count += 1
    else:
        l3 = l[:]
print(count)