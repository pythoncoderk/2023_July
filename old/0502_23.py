n, d = map(int, input().split())
l = [int(input()) for i in range(n-1)]

# print(n, d)
# print(l)
d2 = d
total = d
for i in range(len(l)):
    total += d - l[i]

print(total * d2)