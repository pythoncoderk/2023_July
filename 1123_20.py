n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
# print(l)
l2 = []
for i in range(n):
    l3 = []
    for j in range(l[i][0], l[i][1]+1):
        l3.append(j)
    l2.append(l3)
# print(l2)
l4 = l2[0]
# print(l4)
for i in range(n-1):
    x = set(l2[i+1]) & set(l4)
    l4 = list(x)
if len(l4) != 0:
    print("OK")
else:
    print("NG")