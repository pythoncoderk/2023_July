
n, k = map(int, input().split())
r = list(map(int, input().split()))

print(n, k)
print(r)

l = [1] * n
ans = []
while True:
    if sum(l) % k == 0:
        ans.append(l)
        if 