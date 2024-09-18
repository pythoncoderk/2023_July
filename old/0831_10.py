n = int(input())

d = {}
for i in range(n):
    x = input().split()
    d[x[0]] = x[1]
y = input()
print(d[y])
