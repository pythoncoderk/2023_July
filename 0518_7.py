n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])

l2 = sorted(l, key=lambda x:x[0])

# print(n)
# print(l2)

total = 0
for i in range(n):
    total += l[i][1]

final = total % n

# print(final)

print(l2[final][0])