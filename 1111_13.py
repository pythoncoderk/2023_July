n = int(input())
l = [int(input()) for i in range(n)]
x = 1
while x != n:
    for i in range(x):
        print(l[x] * (l[i]))
    x += 1