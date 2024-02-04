m, n, x = map(int, input().split())
l = [int(input()) for i in range(m)]
n -= 1
x1 = x
# print(m, n, x)
# print(l)
y = 0

count = 0
while l:
    if y <= 0 and len(l) >= 1:
        y = l.pop(0)
    x1 -= y
    if x1 > 0:
        count += 1
        y = l.pop(0)
    if x1 <= 0 and n > 0:
        n -= 1
        x1 = x
    elif n <= 0 and x1 <= 0:
        break

print(count)

