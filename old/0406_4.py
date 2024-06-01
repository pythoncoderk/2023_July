n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

l2 = [[j for j in range(l[i][0], l[i][1]+1)] for i in range(n)]
# print(l2)

total = []
for i in range(n):
    for j in range(len(l2[i])):
        total.append(l2[i][j])
# print(total)

l_f = [total.count(total[i]) for i in range(len(total))]
# print(l_f)

if n in l_f:
    print("OK")
else:
    print("NG")