n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

one = 0
two = 0

for i in range(n):
    for j in range(len(l[i])-1):
        l[i][j+1] = int(l[i][j+1])

# print(l)

for i in range(n):
    if l[i][0] == "SET":
        if l[i][1] == 1:
            one = l[i][2]
        else:
            two = l[i][2]
    elif l[i][0] == "ADD":
        two = one + l[i][1]
    elif l[i][0] == "SUB":
        two = one - l[i][1]
print(f"{one} {two}")