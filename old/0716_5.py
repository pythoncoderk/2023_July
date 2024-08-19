l = list(map(int, input().split()))
n = int(input())
l2 = [list(map(str, input().split())) for i in range(n)]

for i in range(n):
    for j in range(len(l2[i])):
        if j != 0:
            l2[i][j] = int(l2[i][j])

# print(l)
# print(n)
# print(l2)

count = 0
for i in range(n):
    if l2[i][1] <= l[0] <= l2[i][2]:
        if l2[i][3] <= l[1] <= l2[i][4]:
            if l2[i][5] <= l[2] <= l2[i][6]:
                print(l2[i][0])
                count += 1

if count == 0:
    print("no evolution")
