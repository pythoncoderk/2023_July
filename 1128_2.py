n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
# print(n)
# print(l)
l2 = []
for i in range(n):
    l2.append(l[i][1])
# print(l2)
r = l2.count("R")
ll = l2.count("L")
if r == 0 or l == 0:
    print(0)
elif r > ll:
    print(ll)
elif r < ll:
    print(r)
else:
    print(r)