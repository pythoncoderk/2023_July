x, y = map(int, input().split())

if x > y:
    if y + 3 > x:
        print("Yes")
    else:
        print("No")
else:
    if x + 3 > y:
        print("Yes")
    else:
        print("No")