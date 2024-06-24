n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    if l[i][0] == "SET":
        l[i][1] = int(l[i][1])
        l[i][2] = int(l[i][2])
    else:
        l[i][1] = int(l[i][1])

# print(l)

l2 = [0, 0]

for i in range(n):
    if l[i][0] == "SET":
        l2[l[i][1] - 1] = l[i][2]
    elif l[i][0] == "ADD":
        l2[1] = l2[0] + l[i][1]
    elif l[i][0] == "SUB":
        l2[1] = l2[0] - l[i][1]

print(l2[0], l2[1])