n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)

l2 = []
for i in range(n):
    if l[i][0] == "1":
        l2.insert(0, l[i][1])
    elif l[i][0] == "2":
        print(l2[0])
    elif l[i][0] == "3":
        l2.pop(0)
