n, s, k = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
# print(n,s,k)
# print(l)
l2 = []
for i in range(n):
    x = l[i][0] * l[i][1]
    l2.append(x)
total = sum(l2)
if total < s:
    print(total + k)
else:
    print(total)
