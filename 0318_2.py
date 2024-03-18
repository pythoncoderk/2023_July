n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

l2 = sorted(l, key=lambda x: (x[0], x[1], x[2]), reverse=True)
# print(l2)

for i in range(n):
    print(*l2[i])