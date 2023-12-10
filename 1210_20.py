n = int(input())
if n % 4 == 0:
    if n % 400 == 0:
        print("Yes")
    elif n % 100 == 0:
        print("No")
    else:
        print("Yes")
else:
    print("No")