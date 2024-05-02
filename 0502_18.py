n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

l2 = [[j for j in range(l[i][0], l[i][1]+1)] for i in range(n)]

# print(l2)

x = set(l2[0])
for i in range(n):
    x2 = set(l2[i])
    x = x & x2
if len(x) == 0:
    print("NG")
else:
    print("OK")