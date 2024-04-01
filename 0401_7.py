n, v = map(int, input().split())

l = list(map(int, input().split()))

for i in reversed(range(n)):
    x = l[i]
    if x == v:
        print(i)
        exit()

print(-1)