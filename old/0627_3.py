n, m = map(int, input().split())
l = [int(input()) for i in range(m)]

# print(n, m)
# print(l)

for i in range(m):
    x = (l[i] // n) * n
    y = x + n
    if abs(x - l[i]) < abs(y - l[i]):
        answer = x
    else:
        answer = y

    print(n if answer == 0 else answer)
