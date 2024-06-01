n = int(input())
m = int(input())

if n % 2 != 0 and m % 2 != 0:
    if n % m != 0:
        print("yes")
    else:
        print("no")
elif n % 2 != 0 and m % 2 == 0:
    if n % m != 0:
        print("yes")
    else:
        print("no")
elif n % 2 == 0 and m % 2 == 0:
    if n % m != 0:
        print("yes")
    else:
        print("no")
elif n % 2 == 0 and m % 2 != 0:
    if n % m != 0:
        print("yes")
    else:
        print("no")
