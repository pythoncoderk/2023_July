n = int(input())
l = [list(input()) for i in range(n)]
l2 = [list(input()) for i in range(n)]

# print(n)
# print(l)
# print(l2)

for i in range(n):
    for j in range(n):
        if l[i][j] != l2[i][j]:
            print(i+1, j+1)