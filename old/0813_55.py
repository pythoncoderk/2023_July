n, k = map(int, input().split())
l = list(map(str, input().split()))
l.sort()
print(l[k - 1])