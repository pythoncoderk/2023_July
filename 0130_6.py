n = int(input())
l = list(map(int, input().split()))
x = 0
for i in range(n):
    x += l[i]
print(x)