n, a = map(int, input().split())
l = list(map(int, input().split()))

print(n, a)
print(l)

l2 = [0] * (max(l) + a + 1)

for i in range(n):
    l2[l[i]] += 1
    l2[l[i] + a] -= 1

print(l2)

x = 0
for i in range(len(l2)):
    l2[i] += x
    x = l2[i]

print(l2)