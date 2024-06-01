n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)

q = []
for i in range(n):
    if l[i][0] == "1":
        q.append(l[i][1])
    elif l[i][0] == "2":
        print(q[0])
    elif l[i][0] == "3":
        q.pop(0)