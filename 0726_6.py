h, w, n = map(int, input().split())

l = [[0] * (w + 1) for i in range(h + 1)]

# print(l)

for i in range(1, len(l)):
    l[i] = [0] + list(map(int, input().split()))
    for j in range(1, len(l[i])):
        l[i][j] += l[i - 1][j] + l[i][j - 1] - l[i - 1][j - 1]

for _ in range(n):
    x, y = input().split()
    print(l[int(x)][int(y)])