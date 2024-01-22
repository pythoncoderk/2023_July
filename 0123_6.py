l1 = list(map(int, input().split()))
n = int(input())
l2 = [list(map(int, input().split())) for i in range(n)]

# print(l1)
# print(n)
# print(l2)

for i in range(n):
    counts_l = 0
    for j in range(len(l1)):
        if l2[i][j] in l1:
            counts_l += 1
    print(counts_l)