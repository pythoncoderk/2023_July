l = list(map(str, input().split()))

l2 = l[::]
l2.sort()

print("Yes" if l == l2 else "No")