a, d, g = map(int, input().split())
n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(a, d, g)
# print(n)

l2 = [[l[i][j] if j == 0 else int(l[i][j]) for j in range(7) ] for i in range(n)]
# print(l2)
count = 0
for i in range(n):
    for j in range(1):
        if l2[i][1] <= a <= l2[i][2] and l2[i][3] <= d <= l2[i][4] and l2[i][5] <= g <= l2[i][6]:
            print(l2[i][0])
            count += 1
if count == 0:
    print("no evolution")