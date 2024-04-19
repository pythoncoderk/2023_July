n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)
win = 0
for i in range(n):
    if l[i][0] == "G":
        if l[i][1] == "C":
            win += 1
    elif l[i][0] == "C":
        if l[i][1] == "P":
            win += 1
    elif l[i][0] == "P":
        if l[i][1] == "G":
            win += 1
print(win)