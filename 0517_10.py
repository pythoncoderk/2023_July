n, q = map(int, input().split())
l = list(map(int, input().split()))
l2 = [list(map(int, input().split())) for i in range(q)]
x = 0
cumulative_sum = []
for i in range(n + 1):
    if i == 0:
        cumulative_sum.append(0)
    else:
        x += l[i - 1]
        cumulative_sum.append(x)

# print(n, q)
# print(l)
# print(l2)
# print(cumulative_sum)

for i in range(q):
    print(cumulative_sum[l2[i][1]] - cumulative_sum[l2[i][0] - 1])