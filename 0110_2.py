n, x = map(int, input().split())
l = list(map(int, input().split()))

l2 = [l[i] for i in range(n) if l[i] != x]
print(*l2)