n, k = map(int, input().split())
l = [int(input()) for _ in range(n)]

l2 = [0] + l[::]

for i in range(1, n + 1):
    l2[i] += l2[i - 1]

for _ in range(k):
    print(l2[int(input())])