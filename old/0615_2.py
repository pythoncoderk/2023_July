n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)


def loop(x, y):
    count = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1
    return count



count = 0
for i in range(n):
    if l[i][0] == l[i][1]:
        count += 2
    elif len(l[i][0]) != len(l[i][1]):
        count += 0
    elif loop(l[i][0], l[i][1]) == 1:
        count += 1

print(count)
