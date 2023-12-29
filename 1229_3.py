n = int(input())
l = list(map(int, input().split()))

if l[0] <= n:
    print(n * l[1])
else:
    print(n * l[2])