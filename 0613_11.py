xc, yc, r_1, r_2 = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(xc, yc, r_1, r_2)
# print(n)
# print(l)

for i in range(n):
    print("yes" if r_1 ** 2 <= (l[i][0] - xc) ** 2 + (l[i][1] - yc) ** 2 <= r_2 ** 2 else "no")