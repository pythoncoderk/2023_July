n = int(input())
l = [list(map(int, input().split())) for i in range((n * (n-1))//2)]

# print(n)
# print(l)
l = [[l[i][0]-1, l[i][1]-1] for i in range((n * (n-1))//2)]
l2 = [["-" for j in range(n)] for i in range(n)]

# print(l)
# print(l2)

for i in range(len(l)):
    l2[l[i][0]][l[i][1]] = "W"
    l2[l[i][1]][l[i][0]] = "L"

for i in l2:
    print(*i)