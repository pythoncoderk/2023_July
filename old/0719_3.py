l = list(map(int, input().split()))

l2 = l[::]
l2.sort()

print("Yes" if l[1] == l2[1] else "No")

