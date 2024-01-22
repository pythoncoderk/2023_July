n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
# print(l)

x = 0
y = 0

for i in range(n):
    if l[i][0] == "SET":
        if l[i][1] == "1":
            x = l[i][2]
        else:
            y = l[i][2]
    elif l[i][0] == "ADD":
        x = int(x)
        l[i][1] = int(l[i][1])
        y = x + l[i][1]
    else:
        x = int(x)
        l[i][1] = int(l[i][1])
        y = x - l[i][1]
print(f"{x} {y}")