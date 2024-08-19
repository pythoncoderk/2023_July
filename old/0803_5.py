n = int(input())
l = list(map(int, input().split()))

for i in range(0, 10):
    if i == 9:
        print(l.count(i))
    else:
        print(l.count(i), end=" ")