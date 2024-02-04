n = int(input())
l = list(map(int, input().split()))

sum_l = 0
sum_l_p = 0
for i in range(n):
    sum_l += l[i]
    if sum_l < sum_l_p:
        sum_l_p = sum_l
# print(sum_l_p)

sum_l_p = abs(sum_l_p)
print(sum(l) + sum_l_p)