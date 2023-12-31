xc, yc, r1, r2 = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(xc, yc, r1, r2)
# print(n)
# print(l)

for i in range(n):
    if r1 ** 2 <= ((l[i][0] - xc) ** 2) + ((l[i][1] - yc) ** 2) and r2 ** 2 >= ((l[i][0] - xc) ** 2) + ((l[i][1] - yc) ** 2):
        print("yes")
    else:
        print("no")

