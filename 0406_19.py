n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
print(l)

l2 = [l[i][1] for i in range(n)]
l2 = set(l2)
l2 = list(l2)
l2.sort()

print(l2)

l3 = []
for i in range(len(l2)):
    if l2[i]