n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])

# print(n)
# print(l)

l2 = [l[i][0] for i in range(n)]

s = set(l2)
s = list(s)
# print(s)

l3 = []
for i in range(len(s)):
    count = 0
    for j in range(n):
        if s[i] == l2[j]:
            count += 1
    l3.append(count)

max_name = max(l3)
for i in range(len(s)):
    if max_name == l3[i]:
        print(s[i])

l4 = []
for i in range(len(s)):
    count = 0
    for j in range(n):
        if s[i] == l[j][0]:
            count += l[j][1]
    l4.append(count)

final_max = max(l4)
for i in range(len(l4)):
    if final_max == l4[i]:
        print(s[i])
        break
