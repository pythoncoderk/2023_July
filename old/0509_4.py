n, q = map(int, input().split())
l = list(map(int, input().split()))
l2 = [list(map(int, input().split())) for i in range(q)]

# print(n, q)
# print(l)
# print(l2)


def cumulative_sum(arr):
    x = 0
    l_sum = []
    for i in range(len(arr)):
        if i == 0:
            l_sum.append(x)
            x += l[i]
            l_sum.append(x)
        else:
            x += arr[i]
            l_sum.append(x)
    return l_sum


cumulative_l = cumulative_sum(l)
for i in range(len(l2)):
    x = cumulative_l[l2[i][1]] - cumulative_l[l2[i][0] - 1]
    print(x)