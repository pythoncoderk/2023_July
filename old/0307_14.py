n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]

# print(l)
# print(l2)
# print(l)
d1 = {l[k][0]: int(l[k][1]) for k in range(n)}
d2 = {l2[k][0]: int(l2[k][1]) for k in range(m)}

# print(d1)
# print(d2)
count = 0
while True:
    for i in range(n):
        if l[i][0] in l2:
            if d2[l[i][0]] - d1[l[i][0]] >= 0:
                d2[l[i][0]] -= d1[l[i][0]]
            else:
                print(count)
                exit()
        else:
            print(count)
            exit()
        count += 1

