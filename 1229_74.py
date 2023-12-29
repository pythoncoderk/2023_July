a, b = map(int, input().split())
x, y = map(int, input().split())

if a > x:
    print("Yes")
else:
    if b >= y:
        print("Yes")
    else:
        print("No")
