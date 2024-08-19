l = input().split()
x = 1
while l:
    y = l.pop(0)
    if x % 3 == 0:
        print(f"{y}")
    else:
        print(y, end=" ")
    x += 1