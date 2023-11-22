a, b, r = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    x = (l[i][0] - a) ** 2 + (l[i][1] - b) ** 2
    if x >= r ** 2:
        print("silent")
    else:
        print("noisy")