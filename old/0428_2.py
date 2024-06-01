n = int(input())
l = list(map(str, input().split()))
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]

# print(n)
# print(l)
# print(m)
# print(l2)

d = {l[k]: 0 for k in range(n)}
# print(d)

for i in range(m):
    d[l2[i][0]] += int(l2[i][1])
# print(d)

sort_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
# print(sort_d)

for i in range(len(sort_d)):
    print(sort_d[i][0])