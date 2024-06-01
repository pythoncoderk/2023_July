n = int(input())
l = [list(map(int, input().split())) for i in range((n * (n-1)) // 2)]
l2 = [["-" for j in range(n)] for i in range(n)]

l1 = [[l[i][0]-1, l[i][1]-1] for i in range((n * (n-1)) // 2)]

# print(n)
# print(l1)
# print(l2)

for i in range(((n * n)-n)//2):
    l2[l1[i][0]][l1[i][1]] = "W"
    l2[l1[i][1]][l1[i][0]] = "L"

for i in range(n):
    print(*l2[i])