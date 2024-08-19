n, x = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, x)
# print(l)

l2 = []
while x > 0:
    a = x // 2
    b = x % 2
    l2.append(b)
    x = a

for i in range(n):
    print(l2[l[i] - 1])