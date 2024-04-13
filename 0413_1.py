n = int(input())
l = [int(input()) for i in range(n)]
m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]

# print(n)
# print(l)
# print(m)
# print(l2)

count_l = [0 for i in range(n)]
# print(count_l)

for i in range(m):
   for j in range(l2[i][0]-1, l2[i][1]):
       if count_l[j] + l2[i][2] <= l[j]:
           count_l[j] += l2[i][2]
       else:
           count_l[j] = l[j]
for i in count_l:
    print(i)