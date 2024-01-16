n = int(input())
l = list(map(int, input().split()))

print(l)

for i in range(n-1):
    for j in range(i):
        