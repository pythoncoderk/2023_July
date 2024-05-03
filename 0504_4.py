n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)

l2 = []
for i in range(n):
    chk = True
    for j in range(2):
        if l[i][j] == "n":
            chk = False
    if not chk:
        l2.append(i+1)
print(len(l2))
for i in range(len(l2)):
    print(l2[i])

