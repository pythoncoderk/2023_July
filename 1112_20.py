n = int(input())
l = list(map(int, input().split()))
l.reverse()
for i in range(n):
    if l[i] % 2 == 1:
        x = l.index(l[i])
        print(n - x)
        break