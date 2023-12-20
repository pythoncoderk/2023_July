n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
l = [[int(l[i][1]), l[i][0]] for i in range(n)]
# d_sort = sorted(l, key=lambda x:x[1], reverse=True)
l.sort(reverse=True)
# print(l)
print(l[1][1])
