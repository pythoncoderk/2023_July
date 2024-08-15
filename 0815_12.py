a, b, c = map(int, input().split())
n = int(input())

l = [list(map(int, input().split())) for i in range(n)]


# print(a, b, c)
# print(n)
# print(l)

total = 9999999999999999999999999
for i in range(n):
    if l[i][1] >= a:
        if l[i][1] + l[i][2] >= a + b:
            if l[i][1] + l[i][2] + l[i][3] >= a + b + c:
                if total > l[i][0]:
                    total = l[i][0]

if total == 9999999999999999999999999:
    total = -1

print(total)