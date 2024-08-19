n, m = map(int, input().split())
l = [int(input()) for i in range(m)]

# print(n, m)
# print(l)

for i in range(m):
    x = (l[i] // n) * n
    y = x + n

    if abs(l[i] - x) < abs(l[i] - y):
        answer = x
    else:
        answer = y

    if answer == 0:
        print(n)
    else:
        print(answer)