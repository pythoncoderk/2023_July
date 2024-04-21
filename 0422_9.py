l = list(input().split())
n = int(input())
l2 = [list(map(str, input().split())) for i in range(n)]

# print(l)
# print(n)
# print(l2)

for i in range(n):
    count = 0
    for j in range(len(l)):
        if l2[i][j] in l:
            count += 1
    print(count)