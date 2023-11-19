x, y = map(int, input().split())
if x >= 25 and y <= 40:
    print("No")
elif x >= 25 or y <= 40:
    print("Yes")
else:
    print("No")