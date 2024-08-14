n = int(input())
l = list(map(int, input().split()))

max_l = 0

for i in range(n):
    total = 0
    x1, x2, x3, x4, x5 = map(int, input().split())
    total += x1 * l[0] + x2 * l[1] + x3 * l[2] + x4 * l[3] + x5 * l[4]
    if max_l < total:
        max_l = total

print(max_l)