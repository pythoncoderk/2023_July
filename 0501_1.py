n, x = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, x)
# print(l)

l2 = []
while x > 0:
    x2 = x % 2
    x //= 2
    l2.append(x2)
# l2.reverse()
# print(l2)

for i in range(n):
    print(l2[l[i]-1])