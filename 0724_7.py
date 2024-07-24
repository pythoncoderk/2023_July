n, k = map(int, input().split())

l = [int(input()) for _ in range(n)]
x = 0
l2 = []
for i in range(n):
    x += l[i]
    l2.append(x)

# print(l2)

for _ in range(k):
    print(l2[int(input()) - 1])