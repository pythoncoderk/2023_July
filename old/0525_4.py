n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

l2 = []
for i in range(n):
    count = 0
    for j in range(n):
        if l[i] < l[j]:
            count += 1
    l2.append(count + 1)

for i in range(n):
    print(l2[i])