l = list(map(int, input().split()))
l.sort()

x = l[2] - l[1]
y = l[1] - l[0]

print("Yes" if x == y else "No")