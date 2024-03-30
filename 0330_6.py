a, d, g = map(int, input().split())
n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

for i in range(n):
    for j in range(1, 7):
        l[i][j] = int(l[i][j])

# print(a, d, g)
# print(n)
# print(l)

count = []
for i in range(n):
    if l[i][1] <= a <= l[i][2] and l[i][3] <= d <= l[i][4] and l[i][5] <= g <= l[i][6]:
        count.append(l[i][0])

if not count:
    print("no evolution")
else:
    for i in range(len(count)):
        print(count[i])

