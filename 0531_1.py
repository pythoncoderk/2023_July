n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

count = 0
for i in range(n):
    if l[i][0] == "G" and l[i][1] == "C":
        count += 1
    elif l[i][0] == "C" and l[i][1] == "P":
        count += 1
    elif l[i][0] == "P" and l[i][1] == "G":
        count += 1

print(count)