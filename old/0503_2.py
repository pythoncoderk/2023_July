n = int(input())
l = [int(input()) for i in range(n)]
l2 = [list(map(int, input().split())) for i in range(n)]
m = int(input())
l3 = [int(input())-1 for i in range(m)]

# print(n)
# print(l)
# print(l2)
# print(m)
# print(l3)

total = 0
for i in range(m-1):
    total += l[l3[i]]
    total += l2[l3[i]][l3[i+1]]
total += l[l3[-1]]
print(total)
