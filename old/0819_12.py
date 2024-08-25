n = int(input())

l = list(map(int, input().split()))

for i in range(n):
    print((i + 1) * l[i])