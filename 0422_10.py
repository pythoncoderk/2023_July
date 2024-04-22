n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)

for i in range(n):
    x = -1
    for j in range(len(l[i])-1):
        l[i][x] = int(l[i][x])
        x -= 1
# print(l)

a = 0
b = 0
for i in range(n):
    if l[i][0] == "SET":
        if l[i][1] == 1:
            a = l[i][2]
        else:
            b = l[i][2]
    elif l[i][0] == "ADD":
        b = a + l[i][1]
    elif l[i][0] == "SUB":
        b = a - l[i][1]

print(f"{a} {b}")



