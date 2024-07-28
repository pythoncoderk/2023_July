h, w, n = map(int, input().split())

l = [[0] + [0 for j in range(h)] for i in range(w + 1)]

print(l)

for i in range(1, len(l)):
    l2 = [0] + list(map(int, input().split()))
    l[i] = l2
    for j in range(1, len(l[i])):
        l[i][j] += l[i - 1][j] + l[i][j - 1] - l[i - 1][j - 1]
