x, y, z = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(x, y, z)
# print(n)
# print(l)

total1 = 0
total2 = 0
total3 = 0
total4 = 0

for i in range(n):
    for j in range(l[i][0], l[i][1]):
        if 0 <= j < 9:
            total1 += 1
        elif 9 <= j < 17:
            total2 += 1
        elif 17 <= j < 22:
            total3 += 1
        else:
            total4 += 1
print((total1 * z) + (total2 * x) + (total3 * y) + (total4 * z))


