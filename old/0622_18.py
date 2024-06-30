n, s, t = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, s, t)
# print(l)

l2 = []
x = 0
for i in range(n):
    y = l[i] + x
    l2.append(y)
    x = y

# print(l2)

count = 0
for i in range(n):
    if s <= l2[i] <= t:
        count += 1

print(count)