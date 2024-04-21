n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]

# print(n)
# print(l)
# print(m)
# print(l2)

l3 = [l[i][0] for i in range(n)]
d = {l[k][0]: int(l[k][1]) for k in range(n)}
d2 = {l2[k][0]: int(l2[k][1]) for k in range(m)}

# print(d)
# print(d2)

l4 = set(l3)
l4 = list(l4)
# print(l4)

count = 0
chk = True
w_i = 0
while chk:
    if l4[w_i] in d2:
        if d2[l4[w_i]] - d[l4[w_i]] >= 0:
            d2[l4[w_i]] -= d[l4[w_i]]
            w_i += 1
        else:
            chk = False
        if w_i >= n:
            w_i = 0
            count += 1
    else:
        break
print(count)