n, s, k = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, s, k)
# print(l)

total = 0
for i in range(n):
    total += l[i][0] * l[i][1]

if total >= s:
    print(total)
else:
    print(total + k)