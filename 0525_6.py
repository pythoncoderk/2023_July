n = int(input())
l = [int(input()) for i in range(n)]
m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]
l3 = [[l2[i][0]-1, l2[i][1]-1] for i in range(m)]

# print(n)
# print(l)
# print(m)
# print(l2)
# print(l3)

l4 = l[::]

# print(l4)

count = 0
for i in range(m):
    l4[l3[i][0]] -= 1
    l4[l3[i][1]] -= 1
    if l4[l3[i][0]] >= 0 and l4[l3[i][1]] >= 0:
        count += 1
        l = l4[::]
    else:
        l4 = l[::]

print(count)