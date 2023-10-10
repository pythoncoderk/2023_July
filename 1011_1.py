n = int(input())
l = list(map(int, input().split()))

x = 0
for i in range(10):
    if i == 9:
        print(l.count(x))
    else:
        print(l.count(x), end=" ")
        x += 1