n = int(input())
l = [int(input()) for i in range(n)]
l2 = [list(map(int, input().split())) for i in range(n)]
m = int(input())
l3 = [int(input()) for i in range(m)]
l3_2 = []
for i in range(len(l3)):
    l3_2.append(l3[i] - 1)

# print(n)
# print(l)
# print(l2)
# print(l3_2)

total = 0
for i in range(len(l3_2)-1):
    total += l2[l3_2[i]][l3_2[i+1]]

# print(sum(l) + total)

for i in range(len(l3_2)):
    total += l[l3_2[i]]

print(total)