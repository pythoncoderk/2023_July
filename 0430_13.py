n = int(input())
l = [list(input().split()) for i in range(n)]
l2 = [[int(l[i][j]) if l[i][j].isdecimal() else l[i][j] for j in range(2)] for i in range(n)]

# print(n)
# print(l2)

l_100 = [i for i in range(1, 101)]
# print(l_100)

for i in range(n):
    for j in range(100):
        if l2[i][0] == ">":
            if l_100[j] <= l2[i][1]:
                l_100[j] = 0
        elif l2[i][0] == "<":
            if l_100[j] >= l2[i][1]:
                l_100[j] = 0
        else:
            if l_100[j] % l2[i][1] != 0:
                l_100[j] = 0
print(max(l_100))