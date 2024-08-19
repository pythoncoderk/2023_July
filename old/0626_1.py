n, m = map(int, input().split())
l = [int(input()) for i in range(m)]

# print(n, m)
# print(l)

for i in range(m):
    x = (l[i] // n) * n
    y = x + n
    x1 = abs(l[i] - x)
    y1 = abs(l[i] - y)
    if y1 == x1:
        answer = y
    elif y1 < x1:
        answer = y
    else:
        answer = x

    if answer == 0:
        print(n)
    else:
        print(answer)


