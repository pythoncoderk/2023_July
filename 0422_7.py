x, y, r1, r2 = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(x, y, r1, r2)
# print(n)
# print(l)

for i in range(n):
    if r1 ** 2 <= ((x - l[i][0]) ** 2) + ((y - l[i][1]) ** 2) <= r2 ** 2:
        print("yes")
    else:
        print("no")

