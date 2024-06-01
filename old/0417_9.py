n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

l2 = []
for i in range(n):
    x = 0
    for j in range(n):
        if l[i] < l[j]:
            x += 1
    l2.append(x)

for i in l2:
    print(i+1)



