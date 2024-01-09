y = int(input())

if y % 4 == 0:
    if y % 400 == 0:
        print("Yes")
    elif y % 100 == 0:
        print("No")
    else:
        print("Yes")
else:
    print("No")