n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
# print(n)
# print(l)
l2 = []
for i in range(n):
    if l[i][0] == 1:
        l2.append(l[i][1])

print(len(l2))
for i in l2:
    print(i)