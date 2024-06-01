n, d = map(int, input().split())
l = [int(input()) for i in range(n-1)]

# print(n, d)
# print(l)

for i in range(n-1):
    l[i] = d - l[i]

print((d + sum(l)) * d)