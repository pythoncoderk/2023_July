n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)

for i in range(n):
    l[i][1] = int(l[i][1])

l_sort = sorted(l, key=lambda x:(x[1]), reverse=True)
# print(l_sort)

print(l_sort[1][0])
