n, k = map(int, input().split())
l = list(map(int, input().split()))
print(n, k)
print(l)
l2 = []
for i in range(n):
    l2.append((l[i] + 1 - l[i]) % k)
print(l2)

print(1 % k)