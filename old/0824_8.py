n, k = map(int, input().split())
l = list(map(int, input().split()))
l2 = l[::-1]
x = l2[:k]
y = l2[k:]

print(*(x[::-1] + y[::-1]))

