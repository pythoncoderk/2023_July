n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
k = int(input())

counts_l = 0

# print(n)
# print(l)

for i in range(n):
    if k >= abs(l[-1][0] - l[i][0]) + abs(l[-1][1] - l[i][1]):
        counts_l += 1
print(counts_l)