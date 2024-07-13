a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())

a1, a2 = abs(a1), abs(a2)
b1, b2 = abs(b1), abs(b2)
c1, c2 = abs(c1), abs(c2)


x = a1 + b1 + c1
y = a2 + b2 + c2

if (x % 2 == 0 and y % 2 == 0) or (x % 3 == 0 and y % 3 == 0):
    print("No")
    exit()

if (x % 3 == 0 and y % 4 == 0) or (x % 4 == 0 and y % 3 == 0):
    print("Yes")
else:
    print("No")