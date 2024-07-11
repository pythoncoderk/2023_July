x, y = map(int, input().split("."))

# print(x, y)

if 0 <= y <= 2:
    print(str(x) + "-")
elif 3 <= y <= 6:
    print(x)
else:
    print(str(x) + "+")