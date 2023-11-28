a, b, r = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
# print(a, b, r)
# print(n)
# print(l)
for i in range(n):
    if ((l[i][0] - a) ** 2) + ((l[i][1] - b) ** 2) >= r ** 2:
        print("silent")
    else:
        print("noisy")