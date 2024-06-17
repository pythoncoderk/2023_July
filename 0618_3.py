n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

for i in range(n):
    for j in range(6):
        if l[i][j].isdecimal():
            l[i][j] = int(l[i][j])

# print(l)



def gedge(arr):
    if arr[0] == "s":
       x = arr[2] + arr[3]
       y = arr[1:]
       if x >= 160 and sum(y) >= 350:
           return 1
       else:
           return 0
    else:
        x = arr[4] + arr[5]
        y = arr[1:]
        if x >= 160 and sum(y) >= 350:
            return 1
        else:
            return 0

count = 0
for i in range(n):
    count += gedge(l[i])

print(count)

