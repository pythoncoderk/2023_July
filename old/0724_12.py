n, k = map(int, input().split())
l = [0] + [int(input()) for _ in range(n)]

# print(l)

for i in range(1, n + 1):
    l[i] = l[i - 1] + l[i]

# print(l)

for _ in range(k):
    print(l[int(input())])