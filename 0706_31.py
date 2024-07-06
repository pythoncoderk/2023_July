n, k, x = map(int, input().split())
l = list(map(int, input().split()))

# print(n, k, x)
# print(l)

l.insert(k, x)

print(*l)
