n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)

x = 0
y = 0

for i in range(n):
    if l[i][0] == "SET":
        if l[i][1] == "1":
            x = int(l[i][2])
        else:
            y = int(l[i][2])
    elif l[i][0] == "SUB":
        y = x - int(l[i][1])
    else:
        y = int(l[i][1]) + x
print(f"{x} {y}")
