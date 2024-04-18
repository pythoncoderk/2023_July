n = int(input())
l = [int(input()) for i in range(n)]
m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]

# print(n)
# print(l)
# print(m)
# print(l2)
l3 = l[::]
count = 0
chk = False
for i in range(m):
    l3[l2[i][0] - 1] -= 1
    l3[l2[i][1] - 1] -= 1
    m_chk = 0
    for i in range(n):
        if l3[i] < 0:
            m_chk += 1
    if m_chk == 0:
        chk = True
    if chk:
        l[l2[i][0] - 1] -= 1
        l[l2[i][1] - 1] -= 1
        count += 1
    l3 = l[::]
    chk = False
print(count)
