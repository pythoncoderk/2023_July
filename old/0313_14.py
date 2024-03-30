a, b = map(int, input().split())

x = a * 2
y = (a * 2) + 1

if b == x or b == y:
    print("Yes")
else:
    print("No")