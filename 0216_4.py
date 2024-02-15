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

time_count = 0
for i in range(m):
    time_count += l[l3[i]]
    if i != m-1:
        time_count += l2[l3[i]][l3[i+1]]
print(time_count)

