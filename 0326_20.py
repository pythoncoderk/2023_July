n = int(input())
l = list(map(int, input().split()))

if n >= l[0]:
    print(n * l[1])
else:
    print(n * l[2])