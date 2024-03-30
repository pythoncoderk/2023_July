x, y = map(int, input().split())
if x - y > 0:
    if x - y <= 3:
        print("Yes")
    else:
        print("No")
else:
    if x - y >= -2:
        print("Yes")
    else:
        print("No")