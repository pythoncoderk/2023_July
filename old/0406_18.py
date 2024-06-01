n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)
for i in range(n):
    xxx = []
    for j in range(n):
        x = abs(l[i][0] - l[j][0]) ** 2
        y = abs(l[i][1] - l[j][1]) ** 2
        xxx.append(x + y)
        max_l = max(xxx)
    for k in range(n):
        if xxx[k] == max_l:
            print(k+1)
            break